from pdfminer.high_level import extract_text
from docx import Document
import io

class ResumeParser:
    def __init__(self, file_storage):
        self.file_storage = file_storage
        self.filename = file_storage.filename.lower()

    def parse(self):
        if self.filename.endswith('.pdf'):
            return extract_text(io.BytesIO(self.file_storage.read()))
        elif self.filename.endswith('.docx'):
            doc = Document(io.BytesIO(self.file_storage.read()))
            return "\n".join([para.text for para in doc.paragraphs])
        else:
            raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")
