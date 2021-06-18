import json

from flask import Flask, jsonify,request
from flask_cors import *
import configs
import convert
from exts import db
from models import Users,Message
from sqlalchemy import and_
app = Flask(__name__)
# 加载配置文件
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object(configs)
# db绑定app
db.init_app(app)

@app.route('/')
def get():
    params = {'id': 2, 'phone': '15187464876'}
    data = Users.query.filter_by(**params).all()
    # print(data)
    # use = Users(id=2,username = 'ypd',phone = 15187464877,password = 12345,role = 'user')
    # db.session.add(use)
    # db.session.commit()
    result = Message.success('请求成功',convert.class_to_dict(data))
    # result = Message.error('请求失败')
    return result

@app.route('/post', methods=['post'])
def post():
    temp = request.get_data()
    form = json.loads(temp.decode("UTF-8"))
    title = form.get('title')
    return Message.success('请求成功',title)

if __name__ == '__main__':
    app.run()
