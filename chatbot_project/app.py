from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)

# Database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='chatbot',
            user='root',
            password='your_mysql_password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    return None

# Store session data
def store_session_data(session_id, query_text, intent_name):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """INSERT INTO session_data (session_id, query_text, intent_name)
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (session_id, query_text, intent_name))
        connection.commit()
        cursor.close()
        connection.close()

# Retrieve session history
def get_session_history(session_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = """SELECT query_text, intent_name FROM session_data
                   WHERE session_id = %s ORDER BY timestamp"""
        cursor.execute(query, (session_id,))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    return []

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    session_id = req['session'].split('/')[-1]
    query_text = req['queryResult']['queryText']
    intent_name = req['queryResult']['intent']['displayName']

    # Store session data
    store_session_data(session_id, query_text, intent_name)

    # Custom logic to handle follow-up questions
    session_history = get_session_history(session_id)
    response_text = "I'm sorry, I don't have the information you're looking for."

    if intent_name == 'Ask for Best Red Wine':
        response_text = "Our best red wine is the Château Margaux."
    elif intent_name == 'Follow-up Question about Wine':
        if any(entry['intent_name'] == 'Ask for Best Red Wine' for entry in session_history):
            response_text = "Château Margaux is a full-bodied red wine with notes of blackberry and oak. It pairs well with grilled meats and aged cheeses."

    return jsonify({'fulfillmentText': response_text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

