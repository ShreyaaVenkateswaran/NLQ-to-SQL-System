from flask import Flask, render_template, request
from db import get_db_connection
from llm import generate_sql_query

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    nl_query = request.form.get("query")  # ✅ Fix: Get data from form instead of JSON

    if not nl_query:
        return "Query cannot be empty", 400

    sql_query = generate_sql_query(nl_query)

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
    except Exception as e:
        return f"SQL Execution Error: {e}", 500
    finally:
        cursor.close()
        conn.close()

    return render_template("results.html", sql_query=sql_query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
