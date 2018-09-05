"""
继承环境可以使用私有属性，避免冲突
"""
class c1:
    def meth1(self):
        self.__x = 88

    def meth2(self):
        print(self.__x)


class c2:
    def metha(self):
        self.__x = 99

    def methb(self):
        print(self.__x)


class c3(c1, c2): pass


i = c3()

i.meth1()

i.metha()

print(i.__dict__)

i.meth2();i.methb()