from fileinput import filename
from PyPDF2 import PdfFileMerger
import os
from pathlib import Path
import shutil

#Colocar el directorio donde se desea unir los PDFs
current_dir = os.path.dirname('')

pdfs=[]

for filename in os.listdir(current_dir):
	if filename.endswith('.pdf'):
        	pdfs.append(filename)
		
merger=PdfFileMerger()

for pdf in pdfs:
	merger.append(pdf)
	print("Merging!")

merger.write('merged.pdf')

print("All done!")

merger.close()