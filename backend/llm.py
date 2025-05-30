import re
import requests

# Configure your Groq API details
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
<<<<<<< HEAD
GROQ_API_KEY = "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" 
=======
GROQ_API_KEY = "---api key---" 
>>>>>>> 81fdc3d67a008e20d4a98d5d833196113e2f7c95

def generate_sql_query(natural_language_query):
    """ Sends a natural language query to the Groq LLM and extracts the SQL query. """
    
    # Construct API request payload
    payload = {
        "model": "llama-3.3-70b-versatile",  
        "messages": [
            {"role": "system", "content": "You are an AI that converts natural language into MySQL queries."},
            {"role": "user", "content": f"Generate only a valid MySQL query without explanation. Do not include markdown. Query: {natural_language_query}"}
        ]
    }
    
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}

    try:
        response = requests.post(GROQ_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        llm_response = response.json()["choices"][0]["message"]["content"]

        # Extract only the SQL query
        cleaned_sql = clean_sql_response(llm_response)
        return cleaned_sql

    except requests.exceptions.RequestException as e:
        print("Error communicating with Groq API:", e)
        return None

def clean_sql_response(llm_response):
    """Extracts only the SQL query from the LLM response."""
    match = re.search(r"```sql\n(.*?)\n```", llm_response, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    return llm_response.split("\n")[0].strip()  

if __name__ == "__main__":
    test_query = "display the names of the employees"
    sql_query = generate_sql_query(test_query)
    print("Generated SQL Query:", sql_query)
