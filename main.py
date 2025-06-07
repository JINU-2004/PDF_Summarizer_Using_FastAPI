import os
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import fitz  # PyMuPDF
import google.generativeai as genai
import uvicorn
from pdf2image import convert_from_bytes
import pytesseract

app = FastAPI()
templates = Jinja2Templates(directory="templates")

GEMINI_API_KEY = "AIzaSyAhmX3uyVgyRc36DXy_mVmr3jhE-UbyxMk"
genai.configure(api_key=GEMINI_API_KEY)

async def generate_summary(text: str):
    """
    Uses the Gemini model to produce an abstractive summary.
    """
    prompt = f"Please provide a concise and clear summary of the following text:\n\n{text}\n\nSummary:"
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return "Error generating summary: " + str(e)

def extract_text_with_ocr(contents: bytes) -> str:
    images = convert_from_bytes(contents)
    ocr_text = ""
    for img in images:
        ocr_text += pytesseract.image_to_string(img) + "\n\n"
    return ocr_text

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "summary": None})

@app.post("/summarize", response_class=HTMLResponse)
async def summarize(request: Request, pdf_file: UploadFile = File(...)):
    contents = await pdf_file.read()
    full_text = ""

    try:
        pdf_document = fitz.open(stream=contents, filetype="pdf")
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            page_text = page.get_text()
            full_text += page_text + "\n\n"
        pdf_document.close()
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "summary": f"Error reading PDF file: {str(e)}"})

    if not full_text.strip():
        full_text = extract_text_with_ocr(contents)

    if not full_text.strip():
        summary = "No readable text found in PDF."
    else:
        summary = await generate_summary(full_text)
        summary = summary.replace("\n", "<br>")

    return templates.TemplateResponse("index.html", {"request": request, "summary": summary})

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
