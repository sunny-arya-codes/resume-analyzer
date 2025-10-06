from flask import Flask, request, render_template
from parser import ResumeParser
from utils import JobMatcher

app = Flask(__name__)
matcher = JobMatcher("../data/jobs.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files['resume']
        parser = ResumeParser(file)
        text = parser.parse()
        matched_jobs = matcher.match(text)
        return render_template("results.html", jobs=matched_jobs.to_dict(orient="records"))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
