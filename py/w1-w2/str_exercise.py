

'''

字符串练习操作

'''


if __name__ == "__main__":

    name = "jinyanSun"
    # name = "jinyanSun {0} {1} {__l}"

    #c开头
    print(name.capitalize()) #首字符大写,其他的都小写
    print(name.count("n")) # 字符出现的次数
    print(name.center(50,"-")) #返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格

    #e开头
    print(name.endswith("un"),name.endswith("l")) #判断字符串是不是以什么为止
    print(name.expandtabs(10)) #把tab键转换成 多少个空格 没什么用
    print(name.encode(),b'avc'.decode(),f'Hi,{name}') #转换成字节  b''字节的字符串，f''格式化数据

    #f开头
    print('n first find',name.find('n')) #查找字符串第一次的索引位置
    # print(name.format(1,2,__l = "ac")) #格式化
    # print(name.format_map({"a":"l","f":"e"})) #格式化

    #i开头
    try:
        print(name.index('m'))#字串位置
    except (KeyError,ValueError,ZeroDivisionError, Exception) as e:
        print(e)
    else:
        print("finished and exec here")
    finally:
        print("exec and finally")
    #todo 异常可以自定义，需要继承Exception
    '''
    在这个例子中，类 Exception 默认的 __init__() 被覆盖。
    当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类:
    '''
    class Error(Exception):
        pass
    class InputError(Error):

        def __init__(self, expression, message):
            self.expression = expression
            self.message = message

        def __str__(self):
            return repr(self.message)

    class TransitionError(Error):

        def __init__(self, previous, next, message):
            self.previous = previous
            self.next = next
            self.message = message

    #todo 手动抛出异常是由raise

    if name.isdigit():
        print(name.isdigit()) #如果字符串只包含数字则返回 True 否则返回 False
    else:
        pass
        # raise InputError(10,"asd")

    # i开头
    print('isalnum',name.isalnum())#英文字符和0-9判断是不是阿拉伯数字小数和整数
    print('isalpha',name.isalpha()) #如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
    print('isdecimal',name.isdecimal())#检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
    print(name.isidentifier()) #判断是不是一个合法的标识符
    print('sun'.islower())#判断是否是小写
    print('112.1'.isnumeric())#判断是否是数字
    print('112.1'.isdigit())#判断是否是数字
    print('My Name Is'.istitle()) #判断是不是每个单词都是开头大写字母
    print('MY NAME IS'.isupper())#判断是不是都是大写
    print(' '.isspace()) #判断是不是空格

    # j开头
    print(' '.join(['1','2'])) #把数组变成字符串
    print(name.ljust(50,'a')) #保证字符串长度是50，不够的在右侧补充a
    print(name.rjust(50,'a')) #保证字符串长度是50，不够的在左侧补充a

    #l开头
    print(name.lower()) #大写变小写
    print(name.upper()) #小写变大写
    # print(name.ljust())
    print(" d as ".strip())#去掉两边的空格
    print(" aaa a ".lstrip())#去掉左边的空格
    print(' aaa vva '.rstrip())#去掉右边的空格

    #m开头
    p = str.maketrans('abcdefghij','0123456789')
    print(name.translate(p))

    #r开头
    print(name.replace('n','6',name.count('n')))#替换字符
    print(name.rfind('n')) #凑后边查返回最右边匹配到的
    print('a,q,w,tr,g'.rsplit(',')) #变成列表

    #s开头方法
    print(name.startswith('j'))#判断不是以什么开头
    # print(name.splitlines()) 使用空行分割成数组
    print(name.swapcase())#大写变小写，小写变大写字母

    #t开头
    p = str.maketrans('abcdefghij', '0123456789')
    print(name.translate(p))

    #u开头
    #name.upper()

    #z开头
    print(name.zfill(30)) #和下边的相同
    print(name.rjust(30,"0"))
