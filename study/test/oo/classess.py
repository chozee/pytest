from test.impmoudle import import1


class Processsor:
    pass

class A:
    attr = 'A'


class B(A):
    pass


class C(A):
    attr = 'C'


class D(B, C):
    pass


# x = D()
# print(x.attr)


class limitr(object):
    __slots__ = ['age', 'name', 'sex']


class newporps(object):
    def getage(self):
        return 40

    age = property(getage, None, None, None)



import sys
print(sys.version, sys.platform)

# x = newporps()
# print(x.age)

class newporps2():
    def getage(self):
        return 40

    age = property(getage, None, None, None)


class newporps3():
    num = 0
    def printNum():
        print('Num of instance:', newporps3.num)

    printNum = staticmethod(printNum)

    def getage(self):
        return 40

    def setsbx(self, value):
        print('set age:', value)
        self._age = value # 如果去掉下划线 死循环 会调用super._setattr_


    age = property(getage, setsbx, None, None)


class AA:
    numIns = 0
    def __init__(self):
        AA.numIns += 1

    def printNumIns(cls):
        print("Num of ins:", cls.numIns, cls)
    printNumIns = classmethod(printNumIns)


class AAA(AA):
    def printNumIns(cls):
        print("extra stuff...", cls)
        AA.printNumIns()

    printNumIns = classmethod(printNumIns)


def testDecorator(cls):
    print('testDecorator.', cls)
    cls.num = 0 # 统一操作
    return cls


@testDecorator
class TestDec:
    pass


class XX():
    a = 1
    b = [1,2]


"""
    partition six test: 1. inherit 
"""
class Adder:
    def add(self, x, y):
        raise NotImplementedError


class ListAddr(Adder):
    def add(self, x, y):
        return x + y


class DictAddr(Adder):
    def add(self, x, y):
        return x + y


class SubAdder(Adder):
    def __init__(self, lister):
        self.data = lister

    def __add__(self, other):
        return self.add(self.data, other)


"""
    2. operation overload
"""

class MyList(list):
    def __init__(self, data):
        self.data = data[:]

    '''
        reload +
    '''
    def __add__(self, other):
        return self.data.append(other)

    """
        reload index
    """
    def __getitem__(self, item):
        return list.__getitem__(self.data, item)

    """
        reload iter
    """
    def __iter__(self):
        pass


class IntList(list):
    def __init__(self, listval):
        self.val = listval

    def __add__(self, other):
        for x in other.val:
            if x not in self.val:
                self.val.append(x)
        return self.val

    def __sub__(self, other):
        tmplist = []
        for x in other.val:
            if x not in self.val:
                tmplist.append(x)
        return tmplist

    def __repr__(self):
        return 'list is %s' % self.val

if __name__ == "__main__":

    ## test attr
    # i = XX()
    # # print('i.a=%s, XX.a = %s' % (i.a, XX.a))
    # print('i.b = %s, XX.b = %s' % (i.b, list(XX.b)))
    # XX.b.append(3)
    # print('i.b = %s, XX.b = %s' % (list(i.b), list(XX.b)))
    #
    # i.b.append(4)
    # print('i.b = %s, XX.b = %s' % (list(i.b), list(XX.b)))
    #
    # j = XX()
    # print('j.b = %s, XX.b = %s' % (list(j.b), list(XX.b)))

    x = [x for x in range(1, 5)]
    y = [y for y in range(3, 6)]
    x = IntList(x)
    y = IntList(y)
    print(x)
    print(y)
    print(x-y)
    print(x+y)



    ## test decorator
    # c = TestDec()

    ## test clss method sub par
    # x, y = AA(), AAA()
    # x.printNumIns()
    # AAA.printNumIns()
    # y.printNumIns()

    # x2 = newporps3()
    # print(x2.age)
    # x2.age = 42

    # print(newporps3.printNum())

    # x = limitr()
    # print(x.age)

    # print(list(x.__dict__)) # error no attribute
    # x.ape = 30 # test slots