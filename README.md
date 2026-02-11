# VCE2PDF_Formatter
A lightweight Python utility to transform exported VCE (Visual CertExam) data into professionally formatted, searchable PDF documents.

## 💡 Why this exists
Most .vce files use proprietary AES-256 encryption, making direct conversion via Python unreliable and prone to breaking with software updates. This tool follows a Hybrid Conversion Workflow:
Export: Use a VCE viewer to save your exam as a raw .txt file.
Format: This script parses that text, applies styling, handles text wrapping, and generates a clean PDF.

## ✨ Features
Auto-Formatting: Automatically detects "Question X" patterns and applies bold headers.
Smart Pagination: Uses multi_cell logic to ensure long questions don't get cut off.
Lightweight: Built using the modern fpdf2 library, requiring no heavy dependencies.
Customizable: Easily modify fonts, colors, or layouts in the ExamPDF class.

## 🚀 Quick Start
1. Prepare your file: Export your VCE content to a text file (e.g., exam.txt).
1. Install dependencies:
```bash
pip install fpdf2
```
1. Run the script:
```bash
python converter.py
```

## 🛠️ Requirements
- Python 3.x
- fpdf2
