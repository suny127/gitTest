import unittest
import requests
import base64
# from CheckPoint import CheckPoint
import client

class Login(unittest.TestCase):
    '''登录接口'''

    def setUp(self):
        self.url = 'http://139.199.132.220:9000/event/api/register/'
        # self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.client = client.Client(url=self.url, method=client.Method.POST, type=client.Type.URL_ENCODE)

    def tearDown(self):
        self.client.result()

    def test_login01(self):
        '''正向登录用例'''
        # url = 'http://139.199.132.220:9000/event/api/register/'
        usrname = 'huice'
        res_password = 'huicehuice!@#'
        p = 'abc' + res_password
        password = base64.b64encode(p.encode('utf-8'))
        password1 = str(password, 'utf-8')
        # headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'username': usrname, 'password': password1}

        client = self.client
        client.data = data
        client.send()
        client.equal(client.status_code, 200)
        client.less_then(client.times, 200)
        client.equal(client.json.get('error_code'), 0)
        client.db_equal(int(client.json.get('uid')), "select id from auth_user where username='huice'")

        client.save(name='uid', value=client.res.json().get('uid'))
        client.save(name='token', value=client.res.json().get('token'))


        # res = requests.post(url=self.url, headers=self.headers, data=data)
        # print(res.text)
        # self.check = CheckPoint()
        # self.check.equal(res.status_code,200)
        # self.check.less_then(int(round(res.elapsed.total_seconds()*1000)), 200)
        # self.check.equal(res.json().get('error_code'),0)
        # self.check.db_equal(int(res.json().get('uid')),"select id from auth_user where username='huice'")
        #
        # self.check.save('uid', res.json().get('uid'))
        # self.check.save('token', res.json().get('token'))


        # self.check.result()
        # self.assertEqual(res.status_code,200)
        # self.assertLess(int(round(res.elapsed.total_seconds()*1000)), 200)
        # self.assertEqual(res.json().get('error_code'),0)

    def test_login02(self):
        '''密码错误'''
        # url = 'http://139.199.132.220:9000/event/api/register/'
        usrname = 'huice'
        res_password = 'uicehuice!@#'
        p = 'abc' + res_password
        password = base64.b64encode(p.encode('utf-8'))
        password1 = str(password, 'utf-8')
        # headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        data = {'username': usrname, 'password': password1}
        client = self.client
        client.data = data
        client.send()
        client.equal(client.status_code, 200)
        client.less_then(client.times, 200)
        client.equal(client.json.get('error_code'), 10000)



        # res = requests.post(url=self.url, headers=self.headers, data=data)
        # print(res.text)
        # check = CheckPoint()
        # self.check.equal(res.status_code, 200)
        # self.check.less_then(int(round(res.elapsed.total_seconds() * 1000)), 200)
        # self.check.equal(res.json().get('error_code'), 10000)
        # self.check.result()
        # self.assertEqual(res.status_code, 200)
        # self.assertLess(int(round(res.elapsed.total_seconds() * 1000)), 200)
        # self.assertEqual(res.json().get('error_code'), 10000)