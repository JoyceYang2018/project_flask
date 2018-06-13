#coding:utf-8

#初始化一个Flask对象
from flask import Flask,request
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)#把程序实例作为参数传给构造函数，初始化主类的实例，创建的对象可以在各个扩展中使用

#路由和视图函数
@app.route('/')
def index():
    #request在一个线程中全局可访问，这就是flask上下文
    user_agent= request.headers.get('User-Agent')
    return '<p>Your Browser is %s</p>'%user_agent

@app.route('/user/<name>')#动态部分，默认是字符串
def user(name):
    return '<h1>Hello, %s!</h1>'%name

if __name__ == '__main__':
    manager.run()#轮询，启用调试模式可以激活调试器和重载程序