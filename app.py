from flask import Flask, request, jsonify, render_template
import re
import requests
from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

app = Flask(__name__)

model = SentenceTransformer('all-MiniLM-L6-v2')

def clean_line(line):
    line = line.strip()
    line = re.sub(r'\d{1,2}:\d{2} (AM|PM)', '', line)
    line = re.sub(r'\d{1,2}-\d{1,2}-\d{4}', '', line)
    line = re.sub(r'http\S+|www\S+|instagram\S+', '', line)
    line = re.sub(r'\b\w{1,2}\b', '', line)
    
    unwanted_patterns = [
        r'^(Untitled|File Edit|Format View|Help|Ln\d|[*()])',
    ]
    if any(re.match(pattern, line) for pattern in unwanted_patterns) or not line:
        return ""
    
    return line

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())  
    return synonyms

def expand_query_with_synonyms(query):
    words = query.split()
    expanded_query = []
    
    for word in words:
        synonyms = get_synonyms(word)
        expanded_query.extend(synonyms if synonyms else [word]) 
    
    return ' '.join(expanded_query)

def check_article(query):
    cleaned_lines = [clean_line(query)]
    matches = 0
    total_articles = 0
    similarity_score = 0  

    for line in cleaned_lines:
        adjusted_query = f"{line} news"
        response = requests.get(f'https://newsapi.org/v2/everything?q={adjusted_query}&sortBy=relevancy&apiKey=c55048718a8641c798a72f9634150263')
        
        api_response = response.json()        
        content = api_response.get('articles', [])

        if content:
            total_articles += len(content)
            for article in content:
                title = article.get('title', '')
                description = article.get('description', '')
                content = article.get('content', '')
                combined_text = f"{title} {description} {content}"
                
                current_similarity_score = util.pytorch_cos_sim(model.encode(line), model.encode(combined_text)).item()
                similarity_score = max(similarity_score, current_similarity_score)  
                
                print(f"Comparing with: {combined_text}")  
                print(f"Similarity Score: {current_similarity_score}")  

                if current_similarity_score >= 0.5:  
                    matches += 1

    match_ratio = matches / total_articles if total_articles > 0 else 0

    if match_ratio > 0.65:
        final_verdict = "True"
    else:
        final_verdict = "False"

    return final_verdict, similarity_score  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/factcheck')
def factcheck():
    return render_template('factcheck.html')

@app.route('/check_article', methods=['POST'])
def check_article_api():
    article_text = request.get_json()['article_text']
    print(f"Received article text: {article_text}")  
    verdict, similarity_score = check_article(article_text)
    print(f"Verdict: {verdict}, Similarity Score: {similarity_score}")  
    return jsonify({'verdict': verdict, ' similarity_score': similarity_score})

if __name__ == '__main__':
    app.run(debug=True)