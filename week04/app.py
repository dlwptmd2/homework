from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기 (불러오기)
@app.route('/')
def homework():
    return render_template('index.html')

#####################################################################################33


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():# 여길 채워나가세요!
    # 먼저 고객이 쓴 주문자 이름 가져오기
    receiver_name = request.form['name_give']
    # 고객이 쓴 수량 가져오기
    receiver_amount = request.form['Howmany_give']
    # 고객이 쓴 주소 가져오기
    receiver_address = request.form['address_give']
    # 고객이 쓴 번호 가져오기
    receiver_phone = request.form['phoneNumb_give']


    #DB에 넣을 정보 하나 하나를 orderdata_one으로 지정하기
    orderdata_one = {'Name': receiver_name,
                     'HowMany':receiver_amount,
                     'Address': receiver_address,
                     'Phone': receiver_phone}

    #몽고DB에 저장하라는 명령 쓰기
    db.orders_in_DB.insert_one(orderdata_one)

    #저장되었는지 확인하기 그리고 성공했으면 성공되었다고 말하기
    #'result'랑 석세스 msg는 원래 저장되어잇는 함수인가????
    return jsonify({'result':'success', 'msg':'주문이 몽고디비에 저장되었다'})




# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
# 1. DB에서 리뷰 정보 모두 가져오기
    orders = list(db.orders_in_DB.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'DBorders': orders})#여기서 DBorders는 내가 임의로 정해도 되는 말인가???
# 여길 채워나가세요!



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)