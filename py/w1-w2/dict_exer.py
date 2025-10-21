


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
    print(dict1.items())

    dict2 = {
        "name11":"lka",
        "name22":"lka1",
    }

    dict1.update(dict2)
    print(dict1)
    print(dict2)