#! /usr/local/bin/python

import getpass

# aaa = input("aaa: ")
#
#
# pwd = getpass.getpass("Pwd: ")

fmt = '''
a : {0}
b : {1}
''' .format("1","2")


fmt1 = '''
a : {__a}
b : {__b}
c : {__c}
''' .format(__a = "1",__b = "2",__c=0.0511)

fmt2 = '''
a : %s
b : %d
c : %.2f
''' % ("1",2,0.0511)

while True:
    print("1")
    break

arr = ["1","2",1]

sl = arr[:2]

if len(sl) != 0 and len(arr) != 0:
    print(arr,sl)

tp = (1,2,3,4,"5")
class AA :


    def AC(self):
        print(123123)

    def Ad(self):
        print(789789)

class CC(AA):
    def __cc__(self):
        print("CC+AA")
    pass


class Ef:
    def __ef__(self):
        print("ef")
    pass


class AC(AA,Ef):
    pass

st = "1,2,3,4,5"

'''
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

# def __aa():

def reverseWords(ipt):

    if not isinstance(ipt,str):
        return ""

    newStr = ipt.split(" ")

    newStr = newStr[-1::-1]

    return " ".join(newStr)

if __name__ == "__main__":
    print(fmt)
    print(fmt1)
    print(fmt2)
    print(arr[2])
    print(sl)
    print(tp)

    aa = AA()
    aa.AC()

    try:
     stArr = st.split(",")
     print(stArr.__eq__(stArr))
    except:
        print(aa.AC())
        raise
    finally:
        print("123")

    rl = r"this is line \n"

    rn = "this is line \n"
    print(rl)
    print(rn)

    bn = "aaadqe"
    bl = bn.encode()
    print(bl.decode())

    # start: end:step
    stp = stArr[0:2:1]

    while False :
        print(False)
    else:
        print(True)

    for i in stArr :
        print(i)
    else:
        print(123)

    word = 'runoob'
    for letter in word:
        print(letter)

    sites = ["Baidu", "Google", "Runoob", "Taobao"]
    for site in sites:
        print(site)

    #  1 到 5 的所有数字：
    for number in range(1, 6):
        print(number)

    # //'步长'
    for i in range(0, 10, 3):
        if i == 3:
            pass
            print("pass: ",i)
        print(i)

    for i in range (0,len(stArr)):
        val = stArr[i]
        if 2 <= int(val):
           print(stArr[i])
    else:
        print("for finished")

    i = 0
    while i < 10:
        print(i)
        i += 1
    else:
        print("while finished")

    dic = {"a":1,"b":2}
    for d in dic:
        print(d)
    else:
        print("finished,dic")

    dicKeys = dic.keys()
    dicVal = dic.values()
    for i in range (0,len(dicKeys)):
        print(i)
        # print(dicVal[i]) 报错

    print(isinstance(CC(),AA))
    print(isinstance(AA(),AA))
    print(isinstance(AA(),CC))
    print(issubclass(CC,AA))
    print(issubclass(AA,CC))
    print(issubclass(bool,int))

    print(aa)
    del aa

    rlrl = rl * 2
    print(rlrl)

    print(arr+arr)
    print(arr*2)

    # Set（集合）
    sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Baidu'}

    print(sites)  # 输出集合，重复的元素被自动去掉

    # 成员测试
    if 'Runoob' in sites:
        print('Runoob 在集合中')
    else:
        print('Runoob 不在集合中')

    # set可以进行集合运算
    a = set('abracadabra')
    b = set('alacazam')

    print(a)

    print("a - b",a-b)  # a 和 b 的差集
    print("b-a",b-a)  # b 和 a 的差集

    print(a | b)  # a 和 b 的并集

    print(a & b)  # a 和 b 的交集

    print(a ^ b)  # a 和 b 中不同时存在的元素

    print(isinstance(1,int))
    print(1 is True)
    print(1 == True)

    del b

    print(5+ 2) #加法
    print(5-2) #减法
    print(5*2) #乘法
    print(5/2) #除法 带小数
    print(5 // 2) #除法 得到整数
    print(5 ** 2) # 幂运算
    print(5 % 2) #模运算

    a, b = 1, 2

    p = 'abcde\n'
    p1 = r"abcde\n"
    print(p)
    print(p1)


    bl = True
    # bl.real()

    ac = AC()

    ac.__ef__()
    ac.Ad()

    lst = ["abc",789,2.23,"runoob",70.2]
    tinyLst = [123,"runoob",789]

    print("=======list=======\n")
    print(lst)
    print(lst[0])
    print(lst[1:3])
    print(tinyLst * 2)
    print(lst + tinyLst) #不去重

    print(reverseWords("I Like Python"))

    tup1 = ()  # 空元组
    tup2 = (20,)  # 一个元素，需要在元素后添加逗号

    tup = (1,2,3)
    # tup.append() 错误
    
    lst.append(1)

