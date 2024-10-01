from flask import Flask, request, jsonify, render_template
import psycopg2 
from flaskwebgui import FlaskUI

app = Flask(__name__) 

def get_db_connection(): 
    conn = psycopg2.connect(
        host='postgres',
        database='db-forum',
        user='root',
        password='root'
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages', methods=['POST'])
def add_messages():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (writer, message) VALUES (%s, %s)", (data['writer'], data['message']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'Message added'}), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM messages;")
    messages = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(messages)

if __name__ == 'main__':
    FlaskUI(app=app).run()
