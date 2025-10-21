


if __name__ == "__main__":
    dict1 = {
        "name1":"abc",
        "name2":"abc1",
        "name3":"abc2",
    }

    for name in dict1:
        print(dict1[name])

    print(str(dict1))
    del dict1["name1"]
    print(str(dict1))
    dict1.pop("name2")
    print(str(dict1))
    dict1.popitem()
    print(str(dict1))


    print(len(dict1))
    print(type(dict1))

    dict1["name5"] = "abc5"
    print(dict1)

    print(dict1.get("name5","abc1")) #获取，没有给默认值
    print("name5" in dict1) #判断是否存在

    print(dict1.values())
    print(dict1.keys())
    print(dict1.items()) #以列表返回一个视图对象
    for idx,item in enumerate(dict1.items()):
        print(1)
        print(idx,item[0],item[1])

    for idx,item in dict1.items():
        print(2)
        print(idx,item)

    for item in dict1:
        print(3)
        print(item,dict1[item])

    dict2 = {
        "name11":"lka",
        "name22":"lka1",
    }

    dict1.update(dict2) #把字典dict2的键/值对更新到dict里
    print(dict1)
    print(dict2)

    print(dict1.setdefault("name123","abc123")) #和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
    print(dict1)

    print(dict.fromkeys([1,2,3],"1"))  #创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值