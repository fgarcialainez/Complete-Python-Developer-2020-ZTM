"""
This module implements the PDF watermarker exercise of the Section 17 of the course.
"""

import PyPDF2


def watermark_pdf():
    template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermarked_output.pdf', 'wb') as file:
            output.write(file)


# Entry point of the script
if __name__ == '__main__':
    # Call the PDF waterkmark function
    watermark_pdf()
