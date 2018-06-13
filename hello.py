#coding:utf-8

#初始化一个Flask对象
from flask import Flask
app = Flask(__name__)


#路由和视图函数
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')#动态部分，默认是字符串
def user(name):
    return '<h1>Hello, %s!</h1>'%name

if __name__ == '__main__':
    app.run(debug=True)#轮询，启用调试模式可以激活调试器和重载程序