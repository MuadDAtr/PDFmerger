import PyPDF2
import sys
import os

merging = PyPDF2.PdfFileMerger()
if not os.path.isdir('new_pdfs'):
    os.mkdir('new_pdfs')
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merging.append(file)
merging.write("new_pdfs/MergedDocument.pdf")