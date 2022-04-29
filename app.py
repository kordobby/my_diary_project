from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.rg2sr.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/login", methods=["POST"])
def main_profile_post():
   name_receive = request.form['name_give']

   profile_list = list(db.login.find({}, {'_id':False}))
   count = len(profile_list) + 1
   doc = {
      'num':count,
      'name':name_receive
   }
   db.login.insert_one(doc)
   return jsonify({'msg': '프로필 저장 완료!'})

@app.route("/login", methods=["PUT"])
def update_profile_post():
   index_receive = request.form['index_give']
   update_receive = request.form['update_give']
   db.login.update_one({'num' : int(index_receive)}, {'$set': {'name': update_receive}})
   return jsonify({'msg': '프로필 저장 완료!'})

@app.route("/login", methods=["GET"])
def main_profile_get():
   profile_list = list(db.login.find({}, {'_id': False}))
   return jsonify({'profiles': profile_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


