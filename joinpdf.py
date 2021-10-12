import os
from PyPDF2 import PdfFileMerger

x = sorted([a for a in os.listdir() if a.endswith(".pdf")])
print(x)
merger = PdfFileMerger()

for pdf in x:
    merger.append(open(pdf, 'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)
os.startfile("result.PDF")