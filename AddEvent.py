import unittest
import requests
import datetime
import hashlib
import client
from CheckPoint import CheckPoint

class AddEvent(unittest.TestCase):
    '''添加会议接口'''
    def setUp(self):
        self.url = 'http://139.199.132.220:9000/event/api/add_event/'
        self.client = client.Client(url=self.url, method=client.Method.POST, type=client.Type.URL_ENCODE)
        # self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        # self.check = CheckPoint()

    def tearDown(self):
        self.client.result()

    def test_addEvent01(self):
        '''正向添加'''
        # url = 'http://139.199.132.220:9000/event/api/add_event/'
        title = 'sy2'
        address = 'bejing'
        add_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
        time = add_hour.strftime('%Y-%m-%d %H:%M:%S')
        sign = self.client.get('token')+'para=address=' + address + '&time=' + time + '&title=' + title
        sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()

        data = {'title': title, 'address': address, 'time': time, 'sign': sign}
        self.client.headers['Cookie'] = 'token=%s;uid=%s' % (self.client.get('token'), self.client.get('uid'))

        client = self.client
        client.data = data
        client.send()
        client.equal(client.status_code, 200)
        client.less_then(client.times, 200)
        client.equal(client.json.get('error_code'), 0)
        client.db_execute("delete from api_event where title = 'sy2'")

        # res = requests.post(url=self.url, headers=self.headers, data=data)
        # print(res.text)
        # self.assertEqual(res.status_code, 200)
        # self.assertLess(int(round(res.elapsed.total_seconds() * 1000)), 200)
        # self.assertEqual(res.json().get('error_code'), 10002)
        # check = CheckPoint()
        # self.check.equal(res.status_code, 200)
        # self.check.less_then(int(round(res.elapsed.total_seconds() * 1000)), 200)
        # self.check.equal(res.json().get('error_code'), 0)
        # self.check.db_execute("delete from api_event where title = 'sy2'")
        # check.result()