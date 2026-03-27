from flask import Flask, request, jsonify 

app = Flask(__name__) 

@app.route('/api/v1/activity', methods=['POST'])
def recieve_activity():
    data = request.json 
    print("\n" + "="*30)
    print("📩 서버에 새로운 데이터 도착!")
    print(f"👤 사원번호: {data.get('emp_id')}")
    print(f"📊 상태: {data.get('status')}")
    print(f"⏰ 시간: {data.get('timestamp')}")
    print("="*30)

    return jsonify({
        "status": "success", 
        "message": "Data recieved safel on Flask Server"
    }), 200 

if __name__ == '__main__':
    print("server is working")
    app.run(host='127.0.0.1', port = 5000, debug=True)