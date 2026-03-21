from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")

@app.route("/")
def home():
    return "DevOps Project Running by Nitin Raut"

@app.route("/health")
def health():
    return "Service is healthy"

@app.route("/db")
def db_test():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database="devopsdb",
            user="devops",
            password="devops"
        )

        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()

        cur.close()
        conn.close()

        return f"PostgreSQL version: {db_version[0]}"

    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
