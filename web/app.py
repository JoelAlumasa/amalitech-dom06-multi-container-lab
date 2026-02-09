import os
import time
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppass")

def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5
    )

@app.route("/")
def home():
    last_err = None
    for _ in range(25):
        try:
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT content FROM messages ORDER BY id DESC LIMIT 1;")
                    row = cur.fetchone()
            msg = row["content"] if row else "No message found"
            return f"{msg}\n"
        except Exception as e:
            last_err = e
            time.sleep(1)
    return f"DB not ready: {last_err}\n", 500

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
