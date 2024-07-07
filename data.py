from sqlalchemy import create_engine, text, insert 

db_connection_string = "mysql+mysqldb://2MarNVgMbkgBoNS.root:RnQDXvM0Zs4GT2DS@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?ssl_mode=VERIFY_IDENTITY&ssl_ca=/etc/ssl/certs/ca-certificates.crt"

engine = create_engine(db_connection_string)
# We are connecting this page with the another one.


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
        row = result.fetchone()
    return row._asdict()


def add_aplication_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(
            f"INSERT INTO applications(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
        )

        conn.execute(
            query,
            {
                "job_id": job_id,
                "full_name": data["full_name"],
                "email": data["email"],
                "linkedin_url": data["linkedin_url"],
                "education": data["education"],
                "work_experience": data["work_experience"],
                "resume_url": data["resume_upload"],
            },
        )
        conn.commit()

