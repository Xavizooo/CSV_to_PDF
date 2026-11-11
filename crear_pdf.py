import csv
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)

with open("datos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    next(lector)
    for fila in lector: 
        frase= f"{fila[0]}, tiene {fila[1]} y vive en {fila[2]}"
        pdf.multi_cell(0, 10, frase, new_x="LMARGIN", new_y="NEXT" )

pdf.output("holaMundo.pdf")