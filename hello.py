#coding:utf-8

#初始化一个Flask对象
from flask import Flask,request,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)

manager = Manager(app)#把程序实例作为参数传给构造函数，初始化主类的实例，创建的对象可以在各个扩展中使用
bootstrap = Bootstrap(app)


#路由和视图函数
@app.route('/')
def index():
    #request在一个线程中全局可访问，这就是flask上下文
    return render_template('index.html')

@app.route('/user/<name>')#动态部分，默认是字符串
def user(name):
    return render_template('user.html',name=name)

#出错时的路由
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

if __name__ == '__main__':
    manager.run()#轮询，启用调试模式可以激活调试器和重载程序