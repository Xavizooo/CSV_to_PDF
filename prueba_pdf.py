from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=14)
pdf.cell(text="Prueba csv to pdf")
pdf.output("prueba_csv_to_pdf.pdf")