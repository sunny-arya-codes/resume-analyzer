import spacy
from sentence_transformers import SentenceTransformer

nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight & fast

class NLPProcessor:
    def __init__(self, text):
        self.text = text

    def extract_entities(self):
        doc = nlp(self.text)
        skills = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "SKILL", "EDUCATION"]]
        return skills

    def get_embedding(self):
        return model.encode(self.text)

