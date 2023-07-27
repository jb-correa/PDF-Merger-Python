from PyPDF2 import PdfFileMerger

pdfs=['*.pdf', '*.pdf']

merger=PdfFileMerger()

for pdf in pdfs:
	merger.append(pdf)

merger.write('merged.pdf')

merger.close()