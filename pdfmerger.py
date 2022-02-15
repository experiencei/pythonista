import pyPDF2
import sys

input = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = pyPDF2.pdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("super.pdf")

pdf_combiner(input)