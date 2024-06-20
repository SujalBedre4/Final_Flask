from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "Id": 1,
        "Title": "NASA Fellowship",
        "Location": "Bengaluru, India",
        "Salary": "Rs. 10,00,000",
    },
    {
        "Id": 2,
        "Title": "Crimson Global Academy Internship",
        "Location": "Bengaluru, India",
        "Salary": "",
    },
    {
        "Id": 3,
        "Title": "NASA Internship Programs for Non-STEM Majors",
        "Location": "Bengaluru, India",
        "Salary": "Rs. 10,00,000",
    },
    {
        "Id": 4,
        "Title": "Data-Science Intern",
        "Location": "Remote",
        "Salary": "Rs. 4,00,000",
    }
]


@app.route("/")
def hello_world():
    return render_template("hello.html", jobs=JOBS, company_name='Astro_Travel')

# This is for viewing the data in the jason forms:
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)