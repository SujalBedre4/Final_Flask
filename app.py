from flask import Flask, render_template, jsonify, request
from data import load_jobs_from_db, load_job_from_db, add_aplication_to_db

app = Flask(__name__)


@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("hello.html", jobs=jobs, company_name="Astro_Travel")


# This is for viewing the data in the jason forms:
@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(load_jobs_from_db())


@app.route("/job/<id>")
def show_jobs(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template("jobpage.html", job=job)


@app.route("/job/<id>/apply", methods=["POST"])
def apply_jobs(id):
    data = request.form
    job = load_job_from_db(id)
    # Store this in the DB
    # Send an email
    # Display an acknowledgement
    # return jsonify(data)

    # After getting the data from the user just add that into the database:
    add_aplication_to_db(id, data)
    return render_template("application_submitted.html", application=data, job=job)
