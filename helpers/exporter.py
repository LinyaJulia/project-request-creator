import docx

def createDocumentFromText(text):
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save("projectBrief.docx")