#华为机试第四题：字符串分隔

#题目描述：
#    •连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
#    •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

#输入描述:
#    连续输入字符串(输入2次,每个字符串长度小于100)

# 输出描述:
#    输出到长度为8的新字符串数组

str1 = input()
str2 = input()
def CutStr(object, num):
    for i in range(0, len(object), num):
        a = object[i:i+num]
        if len(a) < 8:
            print(a + '0' * (8-len(a)))
        else:
            print(a)
CutStr(str1, 8)

CutStr(str2, 8)