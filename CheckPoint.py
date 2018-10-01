#自定义检查点函数--原生断言封装改造
import unittest
import pymysql

class CheckPoint(unittest.TestCase):
    DATA = {}
    def save(self, name, value):
        self.DATA[name] = value

    def get(self, name):
        return self.DATA.get(name, None)

    def __init__(self):
        self.flag = 0
        self._type_equality_funcs = {}
        self.db = pymysql.connect(host='139.199.132.220', user='root', password='123456', db='event')

    def equal(self,f,s):
        try:
            self.assertEqual(first=f,second=s)
            print('检查点成功：实际结果[{f}],预期结果[{s}]'.format(f=f, s=s))
        except:
            print('检查点失败：实际结果[{f}],预期结果[{s}]'.format(f=f, s=s))
            self.flag += 1

    def less_then(self,f,s):
        try:
            self.assertLess(f,s)
            print('检查点成功：实际结果[{f}],预期结果[<{s}]'.format(f=f, s=s))
        except:
            print('检查点失败：实际结果[{f}],预期结果[<{s}]'.format(f=f, s=s))
            self.flag += 1

    def db_execute(self,sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()

    def db_equal(self,f,s):
        # db = pymysql.connect(host='139.199.132.220', user='root', password='123456', db='event')
        # 生成数据库的游标指针对象
        cursor = self.db.cursor()
        cursor.execute(s)
        result = cursor.fetchone()[0]
        try:
            self.assertEqual(f,result)
            print('检查点成功：实际结果[{f}],预期结果[{s}]'.format(f=f, s=result))
        except:
            print('检查点失败：实际结果[{f}],预期结果[{s}]'.format(f=f, s=result))
            self.flag += 1

    def db_equals(self,f,s):
        # db = pymysql.connect(host='139.199.132.220', user='root', password='123456', db='event')
        # 生成数据库的游标指针对象
        cursor = self.db.cursor()
        cursor.execute(s)
        result = cursor.fetchall()
        try:
            self.assertEqual(f,result)
            print('检查点成功：实际结果[{f}],预期结果[{s}]'.format(f=f, s=result))
        except:
            print('检查点失败：实际结果[{f}],预期结果[{s}]'.format(f=f, s=result))
            self.flag += 1

    def result(self):
        self.db.close()
        if self.flag > 0:
            self.assertTrue(False)