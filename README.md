# 🧠 Natural Language to SQL Converter (Flask + MySQL + Groq API)

This is a web-based application that allows users to input **natural language queries** and get back **valid MySQL queries** using a Large Language Model (LLM) via the **Groq API**. It also executes the SQL queries and displays the results from a connected MySQL database. All the changes done to the database is reflected on the tables in MySQL workbench as well as in the web page. 

---

## 📌 Features

- 🗣 Convert plain English into **MySQL queries**
- 🧠 Uses Groq LLM (LLaMA 3) for SQL generation
- ⚙️ Backend in **Flask**
- 🗃 Connected to a **MySQL database**
- 🧩 View SQL and results in a user-friendly frontend

---

## 💻 Getting Started

<ol>
  <li>
    <strong>Clone the Repository</strong><br>
    Command:<br>
    <code>git clone https://github.com/ShreyaaVenkateswaran/NLQ-to-SQL-System.git</code><br>
    <code>cd nl-to-sql</code>
  </li>

  <li>
    <strong>Install Dependencies</strong><br>
    The required dependencies to be downloaded are present in the <code>requirements.txt</code> file.<br>
    Command:<br>
    <code>cd backend</code><br>
    <code>pip install -r requirements.txt</code>
  </li>

  <li>
    <strong>API Setup</strong><br>
    Modify the <code>GROQ_API_KEY</code> variable in <code>llm.py</code> and replace <code>'---api key---'</code> with your actual Groq API key for the model <code>llama-3.3-70b-versatile</code>.
  </li>

  <li>
    <strong>Set Up MySQL Database</strong><br>
    Make sure MySQL is installed and running. Create a database (e.g., <code>sql_ai_db</code>) and populate it with some test tables and data using MySQL Workbench or CLI. Then, update your database connection credentials in <code>db.py</code>:
    <pre><code>
      
mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="sql_ai_db"
)
    </code></pre>
  </li>
</ol>

  
