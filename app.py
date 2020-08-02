from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
#1. 클라이언트가 요청한 이름, 수량, 주소, 전화번호 가져오기
    name = request.form['name']
    count = request.form['count']
    address = request.form['address']
    phone = request.form['phone']
#2. 그 자료를 데이터베이스에 저장하기
    order = {
        'name': name,
        'count': count,
        'address': address,
        'phone': phone
    }
    db.orders.insert_one(order)
#3. 성공여부, 성공 메시지 반환하

    return jsonify({'result': 'success', 'msg' : '주문이 들어왔습니다'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    #1. 모든 orders의 정보를 가져와서 list로 변환합니다
    orders = list(db.orders.find({} , {'_id':0}))
    #2. 성공 메시지와 주문들을 보냅니다o 보여줍니다x
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)