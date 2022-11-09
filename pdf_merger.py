import PyPDF2
import sys
import os

merging = PyPDF2.PdfFileMerger()
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merging.append(file)
    merging.write("MergedDocument.pdf")