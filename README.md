# PDF_Summarizer_Using_FastAPI
Simple PDF Summarizer Using Python Fastapi Framework and Gemini AI

This is a web-based PDF Summarization tool built with **FastAPI**, **Google Gemini AI**, and **OCR (Tesseract)**. It allows users to upload PDF files and instantly get a summarized version of their contents — even if the file contains scanned images or text.

## 🚀 Features

- 📎 Upload and summarize PDF documents
- 🧠 Uses Google Gemini (Generative AI) to generate accurate summaries
- 🖼️ OCR support for scanned PDF content using Tesseract
- 🌐 Simple and responsive HTML UI with Jinja2 templates
- ⚡ FastAPI-powered backend for efficient performance

## 🖥️ Demo UI



> Upload your PDF ➡️ Automatically extracts text ➡️ Summarizes it using Gemini ➡️ Displays it on the same page!

---

## 🧰 Tech Stack

- **Backend:** FastAPI
- **Frontend:** HTML + CSS (Jinja2 Templates)
- **PDF Processing:** PyMuPDF (`fitz`), `pdf2image`
- **OCR:** Tesseract via `pytesseract`
- **AI Model:** Google Gemini API

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/JINU-2004/PDF_Summarizer_Using_FastAPI.git
cd pdf-summarizer
```
### 2. Create a virtual environment in your project folder

```bash
# Create environment named `fastvenv`
python -m venv fastvenv

# Activate the environment
# For Windows:
fastvenv\Scripts\activate
# For macOS/Linux:
source fastvenv/bin/activate
```
### 3. Save the files

```bash
pdf-summarizer/
│
├── main.py                 # FastAPI backend
├── requirements.txt        # Project dependencies
├── templates/
    └── index.html          # HTML UI (Jinja2 template)

```
### 4. Install requirements.txt file

```bash
pip install -r requirements.txt
```
### 5. Run the command in terminal

```bash
uvicorn main:app --reload
```
### 6. open your browser and go to:

```bash
http://127.0.0.1:8000/
```
