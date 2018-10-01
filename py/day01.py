# 检查get请求的参数中是否包含sign,如果包含将参数值替换为空格，重新拼接为参数字符串
# str = 'title=华为春季新品发布会&sign=klklklk&limit=100&status=0&address=国家会议中心&time=2018-03-28'
# # li = str.split('&')
# # for i in range(0,li.__len__()):
# #     if 'sign' in li[i]:
# #         li[i] = 'sign=0'
# # new = '&'.join(li)
# # print(new)

# 给定一个字符串 target = 'hello huice'，从中找出第一个不重复的字符,输出它是第几位
# target='hello huice'
# for i in range(0,target.__len__()):
#     if(target.count(target[i]) == 1):
#         print(i)
#         break

# 去除上一题中的重复字符，得到一个新的字符串
# target='hello huice'
# a = []
# for i in target:
#     if i not in a:
#         a.append(i)
# print(''.join(a))

# 小风车
# li = ['-', '\\', '|', '/']
# while True:
#     for i in li:
#         print(i+'\r',end='')

#冒泡排序（从小到大排序）
# x = [90,32,39,12,13]
# def sort(nums):
#     for i in range(0,len(nums)-1):
#         for j in range(0,len(nums)-1-i):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#     return nums
#
# print (sort(x))

# 0、输入n, 计算1到n的阶乘之和
# sum = 0
# a = 5
# for i in range(1,a+1):
#     b =1
#     for j in range(1,i+1):
#         b = b*j
#     sum +=b
# print(sum)


########################################
# 分别使用while与for循环输出1-100之间的所有偶数

# for i in range(1,101):
#     if i%2 == 0:
#         print(i)

# i = 1
# while i < 101:
#     if i % 2 == 0:
#         print(i)
#     i +=1

# 找100以内最大平方数

# for i in range(1,100):
#     if i*i>99:
#         print((i-1)*(i-1))
#         break

# from math import sqrt
# for i in range(99,1,-1):
#     if sqrt(i) == int(sqrt(i)):
#         print(i)
#         break

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# a = input('请输入字符串：')
# a = str(a)
# space = 0
# digit = 0
# alpha = 0
# other = 0
# for i in a:
#     if i.isspace():
#         space += 1
#     elif i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         alpha += 1
#     else:
#         other += 1
# print ('字符串中包含的空格%s个，数字%s个，英文%s个，其他字符%s个' % (space, digit, alpha,other))

# s = '字符串中包含的空格{space}个，数字{digit}个，英文{alpha}个，其他字符{other}个'
# print(s.format(space=space,digit = digit, alpha = alpha, other = other))

# 4.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
# a = input('请输入5位数：')
# a = str(a)
# if a == a[::-1]:
#     print('%s是回文数' % a)
# else:
#     print('%s不是回文数' % a)

# a = input('请输入5位数：')
# for i in range(len(a)/2):
#     if a[i] == a[-i-1]:
#         pass
#     else:
#         print('%s不是回文数' % a)
#         break
# else:
#     print('%s是回文数' % a)

# 打印出100-999中所有的"水仙花数"，所谓"水仙花数"是指一
# 			  个三位数，其各位数字立方和等于该数本身。例如：
# 			  153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方

# for i in range(100,1000):
#     i = str(i)
#     a = 0
#     for j in range(0,3):
#         a += int(i[j])**3
#     if a == int(i):
#         print(i)

# for a in range(999,101,-1):
#     baiwei = a//100
#     gewei = a %10
#     shiwei = a//10 - baiwei*10
#     if baiwei**3 +gewei**3 +shiwei**3 == a:
#         print(a)


# 输出9*9口诀---杨辉三角
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d\t' % (i,j,i*j),end='')
#     print('\r')

# 7.输出100之内的素数总个数，所谓"素数"是指除了1和它本身以外，不能被任何整数整除的数(1不是素数/质数)，例如17
# sum = 0
# for i in range(1, 101):
#     flag = 0
#     for j in range(1,i+1):
#         if i%j == 0:
#             flag += 1
#     if flag in [1,2]:
#         sum += 1
# print(sum)

# sum = 0
# for i in range(2, 101):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         sum += 1
# print(sum)



# 实心矩形
# a = input('输入两个数，以逗号分隔：')
# x = int(a.split(',')[0])
# y = int(a.split(',')[1])
# for i in range(1, x+1):
#     for j in range(1, y+1):
#         print('*', end='')
#     print('\r')

# 空心矩形
# a = input('输入两个数，以逗号分隔：')
# x = int(a.split(',')[0])
# y = int(a.split(',')[1])
# for i in range(1, x+1):
#     for j in range(1, y+1):
#         if (i not in [1,x]) and (j not in [1,y]):
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print('\r')

# a = input('输入两个数，以逗号分隔：')
# x = int(a.split(',')[0])
# y = int(a.split(',')[1])
# for i in range(1, x+1):
#     for j in range(1, y+1):
#         if (i in [1,x]) or (j in [1,y]):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('\r')

# 1.某市的出租车计费标准为：3公里以内10元，3公里以后每0.5公里加收1元；每等待2.
# 		  5分钟加收1元；超过15公里的加收原价的50%为空驶费。
# 		  要求编写程序，对于任意给定的里程数（单位：公里）和等待时间（单位：秒）计算出应付车费


#2.一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数

# for i in range(1,1001):
#     temp = 0
#     for j in range(1,i):
#         if i%j == 0:
#             temp += j
#     if temp == i:
#         print(i)

# *3.用python实现选择排序
# 			算法如下：[49, 38, 27, 45, 13]
# 			第一趟[13, 49, 38, 27, 45]
# 			第二趟[13, 27, 49, 38, 45]
# 			第三趟[13, 27, 38, 49, 45]
# 			第四趟[13, 27, 38, 45, 49]
# li = [49, 38, 27, 45, 13]
# for i in range(0, len(li)-1):
#     temp = li[i]
#     flag = 0
#     for j in range(i+1, len(li)):
#         if temp > li[j]:
#             temp = li[j]
#             flag = j
#     del (li[flag])
#     li.insert(i,temp)
#     # print(li)
# print(li)

# li = [49, 38, 27, 45, 13]
# for i in range(0, len(li)-1):
#     temp = i
#     for j in range(i+1, len(li)):
#         if li[temp] > li[j]:
#             temp = j
#     li[i],li[temp] = li[temp],li[i]
# print(li)

#4、二分法查询（快速排序）
# 先从待排序的数组中找出一个数作为基准数（取第一个数即可），然后将原来的数组划分成两部分：
# 小于基准数的左子数组和大于等于基准数的右子数组。然后对这两个子数组再递归重复上述过程，
# 直到两个子数组的所有数都分别有序。最后返回“左子数组” + “基准数” + “右子数组”，即是最终排序好的数组。
# def quicksort(nums):
#     if len(nums) <= 1:
#         return nums
#     else:
#         left = []
#         right = []
#         sign = nums.pop()
#         for i in nums:
#             if i < sign:
#                 left.append(i)
#             else:
#                 right.append(i)
#         return quicksort(left)+[sign]+quicksort(right)
#
# nums = [6,1,2,7,9,3,4,5,10,8]
# print(quicksort(nums))


# 大脚超市赊账人员名单如下：
# li =['刘能', '王老七', '谢广坤', '赵玉田', '杨晓燕', '刘大脑袋', '王长贵', '谢飞机', '赵四', '王大拿']
# 大脚想移除掉里面的姓氏重复的人（不考虑复姓），但是对于每种姓氏大脚想保留最后出现的那个人。希望你来帮助她
# print(sorted(li,key=li.index))
# li.sort(key=li.index)
# print(li)


# 2.统计一篇英文文章每个单词的出现频率，并返回出现频率最高的前5个单词及其出现次数(字典形式)
# A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However,
# you may be interested in analyzing other texts from Project Gutenberg. You can browse the catalog of 25,000 free online books
# at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg
# are in English, it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian

# str = '''A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may be interested in analyzing other texts from Project Gutenberg. You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian'''
#
# newstr = str.lower()
# li = newstr.split(' ')
# #
# for i in range(0,len(li)):
#     if li[i].endswith('.') or li[i].endswith(','):
#         li[i] = li[i][0:-1]
#
# newli = {}
# for j in li:
#     newli[j] = li.count(j)
#
# newli = dict(sorted(newli.items(),key=lambda x:x[-1],reverse=True)[0:5])
# print(newli)


# newli = []
# for j in li:
#     if [j,li.count(j)] not in newli:
#         newli.append([j,li.count(j)])
#
# newli = sorted(newli,key=lambda x:x[-1],reverse=True)
#
# dic = {}
# for a in range(0,5):
#     key = newli[a][0]
#     value = newli[a][-1]
#     dic[key] = value
# print(dic)



# 1.编写一组数据，记录组内每个人的语文成绩、数学成绩、英语成绩
# 				data = {
# 		            '小明':{'语文':60, '数学':68, '英语':45},
# 		            '小璐':{'语文':10, '数学':28, '英语':5},
# 		            '小辉':{'语文':44, '数学':86, '英语':73},
# 		            '小亮':{'语文':99, '数学':95, '英语':95},
# 		            '田老师':{'语文':98, '数学':65, '英语':100},
# 		            '刘老师':{'语文':77, '数学':97, '英语':65},
# 		       	}
# 				a.找到平均分不足60分的人，
# 				b.找出各科的最高分,平均分
# 				c.找出各科的学霸

# data = {
#     '小明': {'语文':60, '数学':68, '英语':45},
#     '小璐': {'语文':10, '数学':28, '英语':5},
#     '小辉': {'语文':44, '数学':86, '英语':73},
#     '小亮': {'语文':99, '数学':95, '英语':95},
#     '田老师': {'语文':98, '数学':65, '英语':100},
#     '刘老师': {'语文':77, '数学':97, '英语':65},
# }
#a
# for k,v in data.items():
#     if sum(v.values())/3 < 60:
#         print(k)
#b
# yuwen=[]
# shuxue=[]
# yingyu=[]
# for v in data.values():
#     yuwen.append(v['语文'])
#     shuxue.append(v['数学'])
#     yingyu.append(v['英语'])
# print('语文最高成绩：%s,平均成绩：%s；数学高：%s，平均：%s，英语最高：%s，平均：%s' %
#       (max(yuwen),sum(yuwen)/len(yuwen),
#       max(shuxue), sum(shuxue)/len(shuxue),
#       max(yingyu), sum(yingyu)/len(yingyu)))
#c
# yuwen=[]
# shuxue=[]
# yingyu=[]
# for k,v in data.items():
#     yuwen.append([k, v['语文']])
#     shuxue.append([k, v['数学']])
#     yingyu.append([k, v['英语']])
# print(sorted(yuwen,key=lambda x:x[-1],reverse=True)[0][0])
# print(sorted(shuxue,key=lambda x:x[-1],reverse=True)[0][0])
# print(sorted(yingyu,key=lambda x:x[-1],reverse=True)[0][0])

# class Auto:
#     def __init__(self,bandname):
#         self.bandname = bandname
#         self.speed =0.0
#
#     def start(self):
#         return '%s汽车开始启动'% self.bandname
#
#     def speedup(self):
#         self.speed += 10
#     def stop(self):
#         if self.speed >= 30:
#             self.speed -= 30
#         else:
#             self.speed = 0



# class Zan:
#     def __init__(self,max):
#         self.max = max
#         self.__li = []
#
#     def setter(self,a):
#         if not self.__ismax():
#             self.__li.append(a)
#         else:
#             print('超出栈极限')
#     def getter(self):
#         if len(self.__li) == 0:
#             print('栈无值')
#         else:
#             self.__li.pop()
#
#     def __ismax(self):
#         if self.max == len(self.__li):
#             return True
#         else:
#             return False
#     def __str__(self):
#         return ''.join(self.__li)

# 编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数"的异常-------笔试题
# def sub(a,b):
#     if a < b:
#         raise Exception('被减数不能小于件数')
#     else:
#         return a - b
#
# 编写一个计算加法的方法，接收键盘输入的两个数字，进行加法运算，当输入的有非数字时，通过异常处理机制使程序正常运行(返回0)
# def sum():
#     a = input('请输入两个数字,以逗号分隔:')
#     li = a.split(',')
#     if len(li) == 2:
#         res = 0
#         try:
#             res = int(li[0]) + int(li[1])
#         except Exception:
#             pass
#         return res
#     else:
#         print('输入位数错误')

# 3.创建一个用户注册服务（server），其中有一个register方法。当用户名小于6位时，抛出自定义异常
# 		  系统异常NameError的子类UserNameError，显示错误信息：用户名不能小于6位--------穷游网笔试
class Server:
    def register(self,username):
        if len(username)<6:
            raise UserNameError('用户名不能小于6位')

class UserNameError(NameError):
    def __init__(self,msg):
        print(msg)
Server().register('sdf')









