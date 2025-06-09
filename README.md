   # 🧠 Natural Language to SQL Converter (Flask + MySQL + Groq API)

This is a web-based application that allows users to input **natural language queries** and get back **valid MySQL queries** using a Large Language Model (LLM) via the **Groq API**. It also executes the SQL queries and displays the results from a connected MySQL database. All the changes done to the database is reflected on the tables in MySQL workbench as well as in the web page. 


## 📌 Features

- 🗣 Convert plain English into **MySQL queries**
- 🧠 Uses Groq LLM (LLaMA 3) for SQL generation
- ⚙️ Backend in **Flask**
- 🗃 Connected to a **MySQL database** showing results dynamically
- 🧩 View SQL and results in a user-friendly frontend
- 💻 View results in table present in the MySQL workbench in addition to webpage.


## 🚀 Demo
This Demo shows the sql operation results in real time on a web page.
![Demo](./assets/demo.gif)

## 💻 Getting Started

<ol>
  <li>
    Clone the Repository  
    <br><br>
    <code>git clone https://github.com/ShreyaaVenkateswaran/NLQ-to-SQL-System.git</code><br>
    <code>cd nl-to-sql</code>
  </li>

  <br>

  <li>
    Install Dependencies  
    <br><br>
    Navigate to the backend folder and install the dependencies listed in <code>requirements.txt</code>  
    <br><br>
    <code>cd backend</code><br>
    <code>pip install -r requirements.txt</code>
  </li>

  <br>

  <li>
    API Setup  
    <br><br>
    Open <code>llm.py</code> and replace <code>'---api key---'</code> in the <code>GROQ_API_KEY</code> variable with your actual Groq API key for the model <code>llama-3.3-70b-versatile</code>.
  </li>

  <br>

  <li>
    Set Up MySQL Database  
    <br><br>
    Ensure MySQL is installed and running. Create a database (e.g., <code>sql_ai_db</code>) and populate it with test tables and data using MySQL Workbench.<br><br>
    Update database credentials in <code>db.py</code>:
    <pre><code>
mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="sql_ai_db"
)
    </code></pre>
  </li>

  <br>

  <li>
    Run the App  
    <br><br>
    <code>cd backend</code><br>
    <code>python app.py</code>
  </li>

  <br>

  <li>
    Query the LLM  
    <br><br>
    Enter a natural language query through the UI and the system will automatically generate an SQL query. Make sure to specify the table being operated on in the natural language query.
  </li>
</ol>




  
