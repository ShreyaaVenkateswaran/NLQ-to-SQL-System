# 🧠 Natural Language to SQL Converter (Flask + MySQL + Groq API)

This is a web-based application that allows users to input **natural language queries** and get back **valid MySQL queries** using a Large Language Model (LLM) via the **Groq API**. It also executes the SQL queries and displays the results from a connected MySQL database. All the changes done to the database is reflected on the tables in MySQL workbench as well as in the web page. 

---

## 📌 Features

- 🗣 Convert plain English into **MySQL queries**
- 🧠 Uses Groq LLM (LLaMA 3) for SQL generation
- ⚙️ Backend in **Flask**
- 🗃 Connected to a **MySQL database**
- 💻 View SQL and results in a user-friendly frontend

---

## 📂 Project Structure

project/
│
├── backend/
│ ├── app.py # Main Flask app
│ ├── llm.py # LLM-to-SQL integration using Groq
│ ├── db.py # MySQL database connection
│ ├── requirements.txt
│
├── frontend/
│ ├── templates/
│ │ ├── index.html # Input form
│ │ └── results.html # SQL + query results
│ └── static/
│ └── style.css # Basic styling
│
└── README.md

## 🚀 Getting Started

1. Clone the Repository
command:
git clone [https://github.com/your-username/nl-to-sql.git](https://github.com/ShreyaaVenkateswaran/NLQ-to-SQL-System.git)
cd nl-to-sql

2. Install Dependencies
The required dependencies to be downloaded are present in the requirements.txt file
command:
cd backend
pip install -r requirements.txt

3. API Setup
   Modify the 'GROQ_API_KEY' variable in llm.py file and replace the '---api key---' with an actual api key from groq for the model 'llama-3.3-70b-versatile'

4. Set Up MySQL Database
  
