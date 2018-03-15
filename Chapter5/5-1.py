import re

# 原子的使用

# pattern = 'yue'
# string = 'http://yum.iqianyue.com'
# result1 = re.search(pattern,string)
# print(result1)

# pattern="\n"
# string = '''http://yum.iqianyue.com
# http://baidu.com'''
# result1 = re.search(pattern,string)
# print(result1)

# pattern = '\w\dpython\w'
# string = 'abcdefphp365python_py'
# result1 = re.search(pattern,string)
# print(result1)

# p1 = '\w\dpython[xyz]\w'
# p2 = '\w\dpython[^xyz]\w'
# p3 = '\w\dpython[xyz]\W'
# string = 'abcdefphp365pythony_py'
# r1 = re.search(p1,string)
# r2 = re.search(p2,string)
# r3 = re.search(p3,string)
# print(r1)
# print(r2)
# print(r3)