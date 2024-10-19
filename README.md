# TrueCheck
Our platform aims to empower users with tools to identify false information effectively and efficiently ! 
# TrueCheck

## Overview
TrueCheck is a Python-based tool designed to extract text using Optical Character Recognition (OCR) powered by Tesseract. The captured text is saved locally for further use.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**:
  - PIL (Pillow): for taking screenshot of screen 
  - OpenCV: for converting screenshot into grayscale and removing unwanted areas (Taskbar, Footer, Header etc)
  - Pytesseract: for extracting text using OCR
  - NumPy: for image array manipulations
  - Flask: for hosting the code online on a local server
  - Sentence Transformers: for refining the query provided by the user
  - NLTK: for checking the query with an inbuilt dictionary and for using NLP to refine query 
  - Regular Expression: to remove unwanted characters (Ln,Col,period etc)
  - Requests: for using API to fetch news articles 
## Features
- Screen capture with taskbar removal
- Text extraction from the captured screen
- Automatic saving of extracted text to a file

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/TruthCheck.git

