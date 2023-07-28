from PyPDF2 import PdfFileMerger
import os
from pathlib import Path


ruta=r'C:/Users/jbaut/Desktop/Programing/Python/Udemy-Python Developer/Proyectos/PDF-Merger-Python/pdf-merger-python'

os.path.print


pdfs=[ruta+'/27-07-2023 Factura Vicario.pdf', ruta+'/27-07-2023 Factura Vega.pdf']

merger=PdfFileMerger()

for pdf in pdfs:
	merger.append(pdf)
	print("Merging!")

merger.write('merged.pdf')

print("All done!")

merger.close()