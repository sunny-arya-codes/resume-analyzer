import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from nlp_processor import NLPProcessor

class JobMatcher:
    def __init__(self, jobs_csv):
        self.jobs = pd.read_csv(jobs_csv)
        self.model = NLPProcessor

    def match(self, resume_text, top_n=5):
        resume_emb = NLPProcessor(resume_text).get_embedding().reshape(1, -1)
        self.jobs['embedding'] = self.jobs['description'].apply(lambda x: NLPProcessor(x).get_embedding())
        self.jobs['similarity'] = self.jobs['embedding'].apply(lambda x: cosine_similarity(resume_emb, x.reshape(1, -1))[0][0])
        return self.jobs.sort_values(by='similarity', ascending=False).head(top_n)
