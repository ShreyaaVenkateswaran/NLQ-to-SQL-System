from flask import Flask, render_template, request, jsonify
from db import get_db_connection
from llm import generate_sql_query

app = Flask(__name__)

import os
from flask import Flask, render_template, request, jsonify
from db import get_db_connection
from llm import generate_sql_query

# Set template and static folder paths correctly
app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    nl_query = data.get("query")

    if not nl_query:
        return jsonify({"error": "Query cannot be empty"}), 400

    print(f"Received NL Query: {nl_query}")  # Debugging Line

    sql_query = generate_sql_query(nl_query)
    print(f"Generated SQL Query: {sql_query}")  # Debugging Line

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.commit()
    except Exception as e:
        print(f"SQL Execution Error: {e}")  # Debugging Line
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({"sql_query": sql_query, "results": results})

if __name__ == "__main__":
    app.run(debug=True)
