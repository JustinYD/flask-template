# 建表写在models.py文件里面
import json

from exts import db
import time
class Message:
    def success(msg, data):
        return {
            'msg': msg,
            'data': data,
            'status': 200,
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }

    def error(msg):
        return {
            'msg': msg,
            'status': 404,
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }

def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)
# 用户表
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role = db.Column(db.String(255))
    updatetime = db.Column(db.DateTime(0),onupdate=True,default='CURRENT_TIMESTAMP')
    createtime = db.Column(db.DateTime(0), onupdate=True, default='CURRENT_TIMESTAMP')

    @property
    def json(self):
        return to_json(self, self.__class__)


