import qrcode
from PIL import Image
from reportlab.pdfgen import canvas
import os

# Nombre del archivo con los enlaces
archivo_enlaces = "./enlaces drive.txt"

# Leer el archivo y procesar los enlaces
with open(archivo_enlaces, "r", encoding="utf-8") as f:
    lineas = f.readlines()

for linea in lineas:
    if ": " in linea:  # Verifica que la línea tiene el formato correcto
        tema, enlace = linea.strip().split(": ")
        
        # Crear código QR
        qr = qrcode.make(enlace)
        qr_path = f"{tema}.png"
        qr.save(qr_path)
        
        # Crear PDF
        pdf_path = f"./QR/{tema}.pdf"
        c = canvas.Canvas(pdf_path)
        c.setFont("Helvetica", 16)
        c.drawString(100, 750, tema)  # Agregar título más arriba
        
        # Insertar QR en el PDF con tamaño de 3x3 cm (85x85 píxeles aprox.)
        c.drawImage(qr_path, 100, 650, 85, 85)
        c.save()
        
        # Eliminar la imagen QR temporal
        os.remove(qr_path)

print("PDFs generados correctamente.")
