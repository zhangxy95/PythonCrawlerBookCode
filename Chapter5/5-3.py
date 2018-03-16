import re

# string = "apythonhellopythonhispythonourpythonend"
# pattern = ".python."
#
# result = re.match(pattern,string)
# result2 = re.match(pattern,string).span()
# print(result)
# print(result2)

# string = "hellomypythonhispythonourpythonend"
# pattern = ".python."
#
# result = re.match(pattern,string)
# result2 = re.search(pattern,string)
# print(result)
# print(result2)

string = "hellomypythonhispythonourpythonend"
pattern = re.compile(".python.")
# 找到所有匹配的结果
result = pattern.findall(string)
print(result)