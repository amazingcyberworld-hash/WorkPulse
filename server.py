import psycopg2
from flask import Flask, request, jsonify 

app = Flask(__name__) 

def get_db_connection(): 
    conn = psycopg2.connect(
        host = "localhost",
        database = "WorkPulseDB", 
        user = "postgres",
        password = "postgres", 
        port="5432"
    )
    # conn.set_client_encoding('UTF8')
    
    return conn

@app.route('/api/v1/activity', methods=['POST'])
def recieve_activity():
    data = request.json 

    emp_id = data.get('emp_id')
    status = data.get('status')
    timestamp = data.get('timestamp')

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        sql = "INSERT INTO user_activity (emp_id, status, 'timestamp') VALUES (%s, %s, %s)"
        cur.execute(sql, (emp_id, status, timestamp));
    
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(f"DB ERROR: {e}")
        return jsonify({"status": "fail", "error": str(e)}), 500

    return jsonify({"status":"success", "message": "Saved to PostgresSQL"}), 200 

    
if __name__ == '__main__':
    print("server is working")
    app.run(host='127.0.0.1', port = 5000, debug=True)