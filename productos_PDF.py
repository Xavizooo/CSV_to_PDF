import csv
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)

with open("productos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    next(lector)    
    for linea in lector:
        frase= f"{linea[0]}: ${linea[1]} (cantidad: {linea[2]})"
        pdf.multi_cell(0, 5, frase, new_x="LMARGIN", new_y="NEXT")
pdf.output("productos.pdf") 