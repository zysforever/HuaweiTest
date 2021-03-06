#华为机试第二题：计算字符个数

#题目描述：
#    写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。

#输入描述:
#    第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符。

# 输出描述:
#    输出输入字符串中含有该字符的个数。

a = input()
b = input()
count = 0
for i in range(len(a)):
    if (a.lower()).find(b.lower(), i, i+len(b)) != -1:   #a.lower()将字符串转换为小写
        count += 1
print(count)

#str.find(str1,beg, end):检测字符串str中是否包含指定字符串str1，可指定开始结束范围。
#若指定范围内包含指定字符串，返回的是索引值在字符串中的起始位置；
#若不包含指定字符串或不在指定范围内时，返回-1。