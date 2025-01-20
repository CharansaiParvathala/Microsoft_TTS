def read(file):
    from PyPDF2 import PdfReader
    pdf = PdfReader(file)
    text = ''
    for p in pdf.pages:
        text += p.extract_text()+('\n\n***** End of the Page *****\n\n')
    return text
