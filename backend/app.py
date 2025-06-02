from flask import Flask, render_template, request
from llm import generate_sql_query
import mysql.connector
from flask import Flask, request, jsonify
from flask import request, redirect, url_for


app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

db_connection = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="sql_ai_db"
)
cursor = db_connection.cursor(dictionary=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/query', methods=['POST'])
def query():
    # Get the query from form data (not JSON)
    natural_language_query = request.form.get('query')

    sql_query = generate_sql_query(natural_language_query)
    if not sql_query:
        return render_template("results.html", error="Failed to generate SQL query", sql=None, results=None)

    results = run_query(sql_query)

    # If the result is a list (table), show the table
    if isinstance(results, list):
        return render_template("results.html", sql=sql_query, results=results, message=None, error=None)

    # If it's a dict, it may have a message or error
    if isinstance(results, dict):
        if "error" in results:
            return render_template("results.html", error=results["error"], sql=sql_query, results=None)
        elif "message" in results:
            return render_template("results.html", sql=sql_query, results=None, message=results["message"])

    return render_template("results.html", sql=sql_query, results=results, error=None)

def run_query(sql_query):
    try:
        cursor.execute(sql_query)
        # For SELECT queries fetch all results
        if sql_query.strip().lower().startswith("select"):
            results = cursor.fetchall()
            return results
        elif sql_query.lower().startswith("insert"):
            db_connection.commit()
            return {"message": "New row inserted successfully."}
        elif sql_query.lower().startswith("delete"):
            db_connection.commit()
            return {"message": "Row(s) deleted successfully."}
        elif sql_query.lower().startswith("update"):
            db_connection.commit()
            return {"message": "Row(s) updated successfully."}
        else:
            return {"message": "Query executed successfully."}

    except mysql.connector.Error as err:
        return {"error": str(err)}

def add_employee(name, department, salary):
    conn = db_connection()
    cursor = conn.cursor()
    insert_query = "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, department, salary))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    app.run(debug=True)
