import csv
import os
from tkinter import Tk, filedialog
from fpdf import FPDF

# Ventanas para elegir el CSV y el destino del PDF
root = Tk()
root.withdraw()
root.attributes("-topmost", True)

ruta = filedialog.askopenfilename(
    parent=root,
    title="Elige un CSV",
    filetypes=[("Archivos CSV", "*.csv")]
)
if not ruta:
    exit()

destino = filedialog.asksaveasfilename(
    parent=root,
    title="Guardar PDF como",
    defaultextension=".pdf",
    filetypes=[("Archivos PDF", "*.pdf")]
)
if not destino:
    exit()

# Preparar el PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=14)

# Leer el CSV y escribir cada fila en el PDF
with open(ruta, "r", encoding="utf-8-sig") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        linea = ", ".join(fila)
        pdf.multi_cell(0, 10, linea, new_x="LMARGIN", new_y="NEXT")

# Guardar
pdf.output(destino)

print("Se guardó en:", os.path.abspath(destino))
print("¿Existe?", os.path.exists(destino))