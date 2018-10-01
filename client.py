import requests
import base64
import unittest
import pymysql

class Method:
    GET = 'GET'
    POST = 'POST'

class Type:
    FORM = 'FORM'
    URL_ENCODE = 'URL_ENCODE'
    XML = 'XML'
    JSON = 'JSON'
    FILE = 'FILE'


class Client(unittest.TestCase):
    DATA = {}
    DB = None

    def __init__(self, url, method, type=0):
        self.url = url
        self.method = method
        self.type = type
        self.headers = {}
        self.data = {}
        self.res = None

        self.flag = 0
        self._type_equality_funcs = {}
        # self.db = pymysql.connect(host='139.199.132.220', user='root', password='123456', db='event')

    @property
    def status_code(self):
        return self.res.status_code

    @property
    def text(self):
        return self.res.text

    @property
    def json(self):
        return self.res.json()

    @property
    def times(self):
        return int(round(self.res.elapsed.total_seconds() * 1000))

    def set_header(self,key, value):
        self.headers[key] = value

    def set_data(self,dic):
        if isinstance(dic, dict):
            self.data = dic
        else:
            raise Exception('请求参数请以字典格式传递')

    def send(self):
        if self.method == 'GET':
            self.res = requests.get(url = self.url, headers = self.headers, params=self.data)
        elif self.method == 'POST':
            if self.type == 'FORM':
                self.res = requests.post(url=self.url, headers = self.headers, data=self.data)
            elif self.type == 'FILE':
                self.res = requests.post(url=self.url, headers=self.headers, files=self.data)
            elif self.type == 'URL_ENCODE':
                self.set_header('Content-Type', 'application/x-www-form-urlencoded')
                self.res = requests.post(url=self.url, headers=self.headers, data=self.data)
            elif self.type == 'XML':
                self.set_header('Content-Type', 'text/xml')
                xml = self.data.get('xml')
                if xml:
                    self.res = requests.post(url=self.url, headers=self.headers, data=xml)
                else:
                    raise Exception('xml正文，入参格式：{"xml": "xxx"}')
            elif self.type == 'JSON':
                self.set_header('Content-Type', 'application/json')
                self.res = requests.post(url=self.url, headers=self.headers, json=self.data)

            elif self.type == 0:
                self.res = requests.post(url=self.url, headers=self.headers, data=self.data)
            else:
                raise Exception('正文格式不支持')

        else:
            raise Exception('请求的方法类型不支持')

    # 需求/行为驱动开发 用户怎么方便 怎么开发

    def save(self, name, value):
        Client.DATA[name] = value

    def get(self, name):
        return Client.DATA.get(name, None)

    def equal(self, f, s):
        try:
            self.assertEqual(first=f, second=s)
            print('检查点成功：实际结果[{f}],预期结果[{s}]'.format(f=f, s=s))
        except:
            print('检查点失败：实际结果[{f}],预期结果[{s}]'.format(f=f, s=s))
            self.flag += 1

    def less_then(self, f, s):
        try:
            self.assertLess(f, s)
            print('检查点成功：实际结果[{f}],预期结果[<{s}]'.format(f=f, s=s))
        except:
            print('检查点失败：实际结果[{f}],预期结果[<{s}]'.format(f=f, s=s))
            self.flag += 1

    def db_execute(self, sql):
        cursor = Client.DB.cursor()
        cursor.execute(sql)
        Client.DB.commit()

    def db_equal(self, f, s):
        # db = pymysql.connect(host='139.199.132.220', user='root', password='123456', db='event')
        # 生成数据库的游标指针对象
        cursor = Client.DB.cursor()
        cursor.execute(s)
        result = cursor.fetchone()[0]
        try:
            self.assertEqual(f, result)
            print('检查点成功：实际结果[{f}],预期结果[{s}]'.format(f=f, s=result))
        except:
            print('检查点失败：实际结果[{f}],预期结果[{s}]'.format(f=f, s=result))
            self.flag += 1

    def db_equals(self, f, s):
        # db = pymysql.connect(host='139.199.132.220', user='root', password='123456', db='event')
        # 生成数据库的游标指针对象
        cursor = Client.DB.cursor()
        cursor.execute(s)
        result = cursor.fetchall()
        try:
            self.assertEqual(f, result)
            print('检查点成功：实际结果[{f}],预期结果[{s}]'.format(f=f, s=result))
        except:
            print('检查点失败：实际结果[{f}],预期结果[{s}]'.format(f=f, s=result))
            self.flag += 1

    def result(self):
        # self.db.close()
        if self.flag > 0:
            self.assertTrue(False)





# client = Client(url = 'http://139.199.132.220:9000/event/api/register/',method = Method.POST,type = Type.URL_ENCODE)
#
# usrname = 'huice'
# res_password = 'huicehuice!@#'
# p = 'abc' + res_password
# password = base64.b64encode(p.encode('utf-8'))
# password1 = str(password, 'utf-8')
#
# client.data = {'username': usrname, 'password': password1}
# client.send()
# print(client.json)
