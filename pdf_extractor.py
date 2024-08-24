import pytesseract
from pytesseract import Output
import cv2
import camelot
import PyPDF2
from pdf2image import convert_from_path
import os
import numpy as np

# Function to extract text from the PDF (both searchable text and OCR)
def extract_text_from_pdf(pdf_path):
    text = ""
    
    # Extracting text from the searchable PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    
    # If text extraction via PyPDF2 fails, use OCR as fallback
    if not text.strip():
        images = convert_from_path(pdf_path)
        for image in images:
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            ocr_text = pytesseract.image_to_string(image)
            text += ocr_text
    
    return text

# Function to extract tables from the PDF
def extract_tables_from_pdf(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')
    return tables

# Path to your PDF file
pdf_path = 'your_file.pdf'

# Extract text
text = extract_text_from_pdf(pdf_path)

# Save the extracted text to a .txt file
with open('extracted_text.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(text)

# Extract tables
tables = extract_tables_from_pdf(pdf_path)
print("\nExtracted Tables:")
for i, table in enumerate(tables):
    print(f"Table {i + 1}:")
    print(table.df)  # Print table as a dataframe

    # Optionally, save the table as a CSV file
    table.to_csv(f'table_{i + 1}.csv', index=False)