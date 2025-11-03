
#_*_encoding:utf-8_*_

if __name__ == "__main__":

    # print("file os")
    f = open("test.txt",encoding= "utf8",mode="w+")

    # f.seek()
    #
    str1 = "老吾老,以及人之老,幼无幼，以及人之幼"
    str2 = "不经贫贱难为人,不经世事永天真1"
    f.write(f"{str1}\n{str2}")
    f.flush()
    data =  f.read()
    print(data)
    f.close()