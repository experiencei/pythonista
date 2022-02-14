import pyPDF2

 #rb stands for read binary
with open("dummy.pdf", 'rb') as file:
    reader = pyPDF2.pdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = pyPDF2.pdfFileWriter()
    writer.addPage(page)
    with open("tilt.pdf" , 'wr') as new_file:
        writer.write(new_file)