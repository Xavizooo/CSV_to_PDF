from tkinter import Tk, filedialog

Tk().withdraw()

ruta = filedialog.askopenfilename(
    title="Elige un CSV",
    filetypes=[("Archivos CSV", "*.csv")]
)
print(ruta)
if not ruta:
    exit()

destino = filedialog.asksaveasfilename(
    title="Guardar PDF como",
    defaultextension=".pdf",
    filetypes=[("Archivos PDF", "*.pdf")]
)
print(destino)

if not ruta:
    exit()