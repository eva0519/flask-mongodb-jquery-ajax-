from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    id_receive = 1
    if len(list(db.guest_book.find({}))) > 0:
        id_receive = list(db.guest_book.find({},{'_id':False}).sort('id',-1))[0]['id'] + 1

    doc = {
        'id' : id_receive,
        'name': name_receive,
        'comment': comment_receive
    }
    db.guest_book.insert_one(doc)
    return jsonify({'msg': 'POST 연결 완료!'})


@app.route("/homework", methods=["GET"])
def homework_get():
    guest_book_list = list(db.guest_book.find({},{'_id':False}))
    return jsonify({'guests': guest_book_list})


@app.route('/test', methods=['POST'])
def test_post():
   id = request.form['deleteId']
   print(id)
   db.guest_book.delete_one({'id': int(id)})
   return jsonify({'msg': '삭제 요청을 잘 받았어요'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
