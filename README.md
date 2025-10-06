
# AI-Powered Resume Analyzer & Job Matcher

![AI Resume Analyzer Banner](https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1950&q=80)

## Overview

**AI-Powered Resume Analyzer & Job Matcher** is a full-stack Machine Learning project designed to analyze resumes and match candidates with the most relevant job openings. It leverages **NLP, embeddings, and ML pipelines** to extract skills, education, and experience from resumes, and provides a ranked list of job recommendations.  

The project also features a **modern Liquid Glass UI** for an elegant, professional, and user-friendly experience.

---

## Features

- **Resume Parsing:** Extract text from PDF and DOCX resumes.  
- **NLP Processing:** Identify skills, education, and experience using **SpaCy** and **transformer embeddings**.  
- **Job Matching:** Compare candidate profiles with job descriptions using **cosine similarity**.  
- **Generative AI (Optional):** Summarize resumes using GPT for quick insights.  
- **Cloud-Ready:** Easily deployable on **AWS S3, Lambda, or EC2**.  
- **Interactive Web App:** Upload resumes and view top-matched jobs in a **Liquid Glass-style interface**.  

---

## Tech Stack

- **Language:** Python 3.10+  
- **Web Framework:** Flask  
- **NLP & ML:** SpaCy, HuggingFace Transformers, PyTorch, Scikit-learn  
- **Cloud:** AWS (S3, Lambda, optional SageMaker)  
- **Frontend:** HTML, CSS, Liquid Glass UI  
- **Tools:** Git, Docker (optional)  

---

## Project Structure

```

resume_analyzer/
├── data/
│   ├── resumes/           # Sample resumes (PDF/DOCX)
│   └── jobs.csv           # Job descriptions dataset
├── src/
│   ├── parser.py          # Resume parsing logic
│   ├── nlp_processor.py   # NLP & embeddings
│   ├── matcher.py         # Job matching logic
│   ├── app.py             # Flask web app
├── templates/
│   ├── index.html         # Resume upload page
│   └── results.html       # Matched jobs page
├── .venv/                 # Virtual environment
├── .gitignore
└── README.md

````

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd resume_analyzer
````

2. Create virtual environment and activate:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## Usage

1. Place your resume inside `data/resumes/` folder (PDF or DOCX).
2. Run the Flask app:

```bash
cd src
python3 app.py --port 8000
```

3. Open browser:

```
http://127.0.0.1:8000/
```

4. Upload your resume → view **top matched jobs**.

5. Optional: Use `test_run.py` for CLI-based testing.

## Future Enhancements

* Integrate **GPT-based resume summarizer** for profile highlights.
* Add **pagination and search filters** for large job datasets.
* Deploy as a **full cloud SaaS application** on AWS.
* Add **real-time caching of embeddings** for faster job matching.

---

## Author

**Sunni Kumar** – Machine Learning & Full-Stack AI Developer
[GitHub](https://github.com/sunny-arya-codes) | [LinkedIn](https://www.linkedin.com/in/sunni-kumar/)

---

## License

This project is licensed under the MIT License.
