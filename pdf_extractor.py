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

#do the extarction for all the pdfs in the folder
def extract_text_from_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(pdf_path)
            output_path = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}.txt')
            with open(output_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)

#directory where the pdfs are stored
pdfs_path = '/Users/maxbosetti/Documents/libri_ledro/pdfs'
output_foderl = '/Users/maxbosetti/Documents/libri_ledro/texts'

# check if folder path exists
if not os.path.exists(pdfs_path):
    print(f"Folder '{pdfs_path}' not found.")
    exit()

# folder_path = '~/Documents/libri_ledro/pdfs/'

extract_text_from_folder(pdfs_path, output_foderl)



# # Path to your PDF file
# pdf_path = 'your_file.pdf'

# # Extract text
# text = extract_text_from_pdf(pdf_path)

# # Save the extracted text to a .txt file
# with open('extracted_text.txt', 'w', encoding='utf-8') as text_file:
#     text_file.write(text)

# # Extract tables
# tables = extract_tables_from_pdf(pdf_path)
# print("\nExtracted Tables:")
# for i, table in enumerate(tables):
#     print(f"Table {i + 1}:")
#     print(table.df)  # Print table as a dataframe

#     # Optionally, save the table as a CSV file
#     table.to_csv(f'table_{i + 1}.csv', index=False)