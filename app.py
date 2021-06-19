import json

from flask import Flask, jsonify,request
from flask_cors import *
import configs
import convert
from exts import db
from models import Users,Message
from flask_restful import  Api,Resource,reqparse
from sqlalchemy import and_
app = Flask(__name__)
api=Api(app)
# 加载配置文件
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object(configs)
# db绑定app
db.init_app(app)

class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        args = parser.parse_args()  # 解析参数

class User(Resource):
    def get(self):
        params = {}
        data = Users.query.filter_by(**params).all()
        # data = Users.query.all()
        # print(data)
        # use = Users(id=2,username = 'ypd',phone = 15187464877,password = 12345,role = 'user')
        # db.session.add(use)
        # db.session.commit()
        result = Message.success('get请求成功', convert.class_to_dict(data))
        # result = Message.error('请求失败')
        return result
    def post(self):
        parser = reqparse.RequestParser()  # 对reqparse模块下的RequestParser类进行实例化
        parser.add_argument('username', type=str)  # add_argument方法添加接收参数
        args = parser.parse_args()  # 解析参数
        return Message.success('post请求成功', args)
    def put(self):
        return Message.success('put请求成功')
api.add_resource(User,'/User')


if __name__ == '__main__':
    app.run()

