# PDF Extraction Tool

This tool extracts text and tables from PDF files. It handles both standard PDFs and scanned PDFs using OCR (Optical Character Recognition) with `pytesseract`. Additionally, it extracts tables using `camelot`.

## Features

- **Text Extraction**: Extracts text from standard and scanned PDFs using `PyPDF2` and `pytesseract`.
- **Table Extraction**: Extracts tables from PDFs using `camelot`.
- **Handles Scanned PDFs**: Uses `pytesseract` to extract text from scanned images.

## Prerequisites

You need to have [Conda](https://docs.conda.io/en/latest/miniconda.html) installed to create the environment and manage dependencies.

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```
### Step 2: Create the envrinment
```bash
conda create -n pdf_extraction python=3.8
conda activate pdf_extraction
```
### Step 3: Install packages
```bash
# Install pytesseract, tesseract, opencv, and poppler for OCR and image processing
conda install -c conda-forge pytesseract tesseract opencv poppler

# Install PyPDF2 for text extraction from PDFs
conda install -c conda-forge PyPDF2

# Install camelot and ghostscript for table extraction from PDFs
conda install -c conda-forge camelot-py ghostscript
```

### Step4: check installation
```bash
tesseract --version  # Check Tesseract installation
python -c "import pytesseract, cv2, PyPDF2, camelot"  # Check Python packages
```
Running the Script

After updating the script:

	1.	Place your PDF file in the working directory.
	2.	Adjust the pdf_path variable to point to your PDF file.
	3.	Run the script:

```bash
python pdf_extractor.py
```

