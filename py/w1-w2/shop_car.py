#! /user/bin/python
import copy

if __name__ == "__main__":

    #浅拷贝 用途: 联合账号可以使用
    person = ["name",["money",12]]

    p1 = copy.copy(person)
    p2 = person[:]
    p3 = list(person)

    tpl = (1,2)

    tpl1 = tpl[:-1]

    print(tpl)
    print(tpl1)

    money = input("please input money: ")


    if money.isdigit():
        mny = int(money)
        pass
    else:
        mny = int(money)

    goods = [
        {"id":1,"name":"goods1","money":100},
        {"id":2,"name":"goods2","money":200},
        {"id":3,"name":"goods3","money":300},
    ]

    ids = []
    goodsIdx = {}
    l = len(goods)
    # for idx in range(l):
    for idx,good in enumerate(goods): #todo 这个是把 数组的 key也遍历出来，不加只会遍历数组的值
        print(good)

        print(f"goods:{good['id']},name:{good['name']},money:{good['money']}")

        ids.append(good['id'])
        goodsIdx[good['id']] = idx

    goodsId = input("please input goods id:")

    print(goodsIdx)

    if int(goodsId) in ids and goods[goodsIdx[int(goodsId)]]['money'] <= mny:

        print(f"get it: {goods[goodsIdx[int(goodsId)]]['name']}")
    else:

        print("your money not enough")