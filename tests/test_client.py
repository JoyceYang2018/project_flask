#coding:utf-8



import unittest,re
from app import create_app,db
from flask import url_for
from app.models import User,Role

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_home_page(self):
        response = self.client.get(url_for('main.index'))
        self.assertTrue('Stranger' in response.get_data(as_text=True))



    def test_register_and_login(self):
        #注册一个新用户
        response = self.client.post(url_for('auth.register'),data={
            'email':'john@example.com',
            'username':'john',
            'password':'cat',
            'password2':'cat'
        })
        self.assertTrue(response.status_code == 302)

        #使用新注册的账户登录
        response = self.client.post(url_for('auth.login'),data={
            'email': 'john@example.com',
            'password': 'cat'
        },follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue(re.search('Hello,\s*john!',data))
        self.assertTrue('You have not confirmed your account yet' in data)


        #发送确认令牌，忽略注册时生成的令牌，直接在User实例上调用方法重新生成新令牌
        #还有一个方法，Flask-Mail会保存邮件正文，也可以解析邮件正文来提取令牌
        user=User.query.filter_by(email='john@example.com').first()
        token = user.generate_confirmation_token()
        response = self.client.get(url_for('auth.confirm',token=token),
                                   follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('You have confirmed your account' in data)

        #退出
        response = self.client.get(url_for('auth.logout'),
                                   follow_redirects = True)
        data = response.get_data(as_text=True)
        self.assertTrue('You have been logged out' in data)