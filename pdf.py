import PyPDF2
import sys

from PyPDF2 import PdfFileReader, PdfFileWriter

# inputs = sys.argv[1:]


# with open('dummy.pdf', 'rb') as file:
#     reader = p.PdfFileReader(file)
#     page = reader.getPage(0)
#     # print(reader.getPage(0))
#     page.rotateCounterClockwise(90)
#     writer = p.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)

# pdf combiner
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
#
#
# pdf_combiner(inputs)

# watermark pages
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked.pdf', "wb") as merged_file:
        output.write(merged_file)
