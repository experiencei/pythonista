from tempfile import template
import pyPDF2

#another means of opening 
template = pyPDF2.pdfFileReader(open('super.pdf' , 'rb'))
watermark = pyPDF2.pdfFileReader(open('wtr.pdf' , 'rb'))
output = pyPDF2.pdfFileWriter()


for i in range(template.getNumpages()):
    page = template.getPage
    page.mergepage(watermark.getPage(0))
    output.addpage(page)

    with open('watermarked.pdf' , 'wb') as file :
     output.write(file)
