import unittest
#从小到大排序
x = [90,32,39,12,13]
def sort(nums):
    for i in range(0,nums.__len__()-1):
        for j in range(0,nums.__len__()-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

print (sort(x))


# print (range(0,1))
# sum = 0
# for i in range(1,101):
#     if i%2 == 0:
#         sum = sum - i
#     else:
#         sum = sum +i
# print (sum)
# import pymysql
#
#
# db = pymysql.connect(host='139.199.132.220', user='root',password='123456',db='event')
# # 生成数据库的游标指针对象
# cursor = db.cursor()
# print(cursor.execute('select * from api_event'))
# print(cursor.fetchone())
# db.close()


# class Mytest01(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print('setupClass')
#
#     @classmethod
#     def tearDownClass(cls):
#         print('setupClass')
#
#     def test_case01(self):
#         print('test_case01')
#     def test_case02(self):
#         print('test_case02')
#
# class Mytest02(unittest.TestCase):
#     def test_case03(self):
#         print('test_case03')
#
# if __name__ == '__main__':
#     unittest.main()