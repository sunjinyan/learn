import math
import operator
import os
import sys
from copy import deepcopy

from   module1 import test_a as t1
if __name__ == "__main__":
    print(sys.path)
    print(sys.argv)
    print(t1.package)

    print(type(2**22))
    print(type(2**80))
    print(math.pi)

    # os.system("dir") #执行命令，不保存结果
    # os.popen("dir").read()

    print(52.3*10**2)
    print(52.3E2)

    a , b , c = 1 , 2, 5

    f = b if a < b else c # 如果a 大于 b，那么f=b，否则f=c

    print(f)


    by = b'a b c'
    print(by.decode().split(" "))

    # 传统写法
    n = 10
    if n > 5:
        print(n)

    # 使用海象运算符  3.8 才支持
    # if (n := 10) > 5:
    #     print(n)

    arr = ["1","2","3"]

    arr.insert(0,"5")
    arr.append("6")
    arr.append("6")
    arr.append("6")

    print(" ".join(arr))

    print(arr.count("6"))

    # arr.clear()

    array = ["2","12"]

    print(arr.extend(array))

    arr1 =arr.copy()
    print(arr1)

    arr2 = deepcopy(arr)
    print(arr2)

    arr2.remove("6")
    del arr2[2]
    print(arr2)

    arr[0] = "321"

    print(arr1)

    if "61" in arr :
        print(arr.index("61"))
    else:
        print("not found",arr)

    print(isinstance(arr[0],list))
    print(type(arr))


    #列表比较
    print("operator.eq:", operator.eq(arr,arr1))
    print("operator.eq:", arr == arr1)

    print(max(arr))

    tup = (1,2,3,5,6)

    tls = list(tup)
    print(tup)

    tls.append(7)
    print(tls)