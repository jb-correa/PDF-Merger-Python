from PyPDF2 import PdfFileMerger

ruta=r''

pdfs=[ruta+'.pdf', ruta+'.pdf']

merger=PdfFileMerger()

for pdf in pdfs:
	merger.append(pdf)
	print("Merging!")

merger.write('merged.pdf')

print("All done!")

merger.close()