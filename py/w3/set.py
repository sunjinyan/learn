#! /user/local/bin python

#_*_encoding:utf8_*_




if __name__ == "__main__":

    st = {"1",2,3,100}
    st1 = {"5",6,7,100}

    # print(st)
    # print(st1)

    #交集
    st3 = st & st1
    print(st3)
    print(st.intersection(st1))

    #并集
    st5 = st | st1
    print(st5)
    print(st.union(st1))

    #差集
    st6 = st - st1
    print(st6)
    print(st.difference(st1))

    #对称差集
    st7 = st ^ st1
    print(st7)
    print(st.symmetric_difference(st1))

    #子集
    print( st.issubset(st1) )
    #上级
    print(st.issuperset(st1))


    print(st)
    st.add(111)
    print(st)
    st.remove(111)
    print(st)

    print("a" in st)
    print("1" in st)