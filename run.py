import unittest
from xml.etree import ElementTree as ET
import HTMLTestReportCN
import client
import pymysql
import traceback

if __name__ == '__main__':
    try:
        # suite = unittest.TestSuite()
        # suite.addTest(Login.Login('test_login01'))
        # suite.addTest(Login.Login('test_login02'))
        # suite.addTest(AddEvent.AddEvent('test_addEvent01'))
        # unittest.TextTestRunner.run(suite)
        # suite = unittest.defaultTestLoader.discover(start_dir='./',pattern='test_*.py')
        # unittest.TextTestRunner.run(suite)

        et = ET.parse('./config.xml')

        data_configs = et.findall('.//database/*')
        database = {}
        for d in data_configs:
            database[d.tag] = d.text
        else:
            client.Client.DB = pymysql.connect(host=database.get('host'), user=database.get('user'),
                                               password=database.get('password'), db=database.get('dbname'))

        li = et.findall('.//cases/*')
        # print (li)
        suite = unittest.TestSuite()
        for i in li:
            class_name = i.tag.split('-')[0]
            method_name = i.tag.split('-')[1]
            exec('import %s' % class_name)
            exec("suite.addTest(%s.%s('test_%s'))" % (class_name,class_name,method_name))
        # unittest.TextTestRunner().run(test=suite)
        HTMLTestReportCN.HTMLTestRunner(stream=open('./report.html','wb')).run(test=suite)
    except Exception as e:
        # 捕获异常时，会打印出原始堆栈信息，方法调试，如果直接打印e，只会显示错误提示，没有具体行数和内容
        traceback.print_exc()
        # print(e)
    finally:
        if client.Client.DB:
            client.Client.DB.close()