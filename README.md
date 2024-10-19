# TruCheck
Our platform aims to empower users with tools to identify false information effectively and efficiently ! 
# TruCheck

## Overview
TruCheck is an integrated Python and HTML-based website designed to extract text using Optical Character Recognition (OCR) powered by Tesseract. The captured text is saved locally for further use.

## Tech Stack
- **Language**: Python 3
- **Libraries**:
  - Pillow: for taking screenshot of screen 
  - OpenCV: for converting screenshot into grayscale and removing unwanted areas (Taskbar, Footer, Header etc)
  - Pytesseract: for extracting text using OCR (Optical Character Recognition)
  - NumPy: for image array manipulations
  - Flask: for hosting the code online on a local server
  - Sentence Transformers: for refining the query provided by the user
  - NLTK: for checking the query with an inbuilt word dictionary and for using NLP to refine query 
  - Regular Expression: to remove unwanted characters (Ln,Col,period etc)
  - Requests: for using API to fetch news articles
  - PyQt5: Presents GUI Interface to make our tool user friendly
## Features
- Screen capture with taskbar removal
- Text extraction from the captured screen
- Automatic saving of extracted text to a file
- Notifies the user of the false news.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/TruthCheck.git

