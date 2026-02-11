from fpdf import FPDF

class ExamPDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, 'Certification Exam Export', border=False, ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def convert_vce_txt_to_pdf(input_file, output_file):
    pdf = ExamPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    
    # Read the exported VCE text file
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                # Basic formatting: Bold lines that look like Question headers
                if line.startswith("Question"):
                    pdf.set_font("Arial", 'B', 12)
                    pdf.ln(5) 
                else:
                    pdf.set_font("Arial", size=11)
                
                # Multi_cell handles text wrapping for long questions
                pdf.multi_cell(0, 10, txt=line.strip(), align='L')
        
        pdf.output(output_file)
        print(f"Successfully created: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Usage
convert_vce_txt_to_pdf("my_exam_export.txt", "final_exam.pdf")
