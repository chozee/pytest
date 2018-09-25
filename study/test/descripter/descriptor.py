
class Descriptor(object):
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')


class Subject:
    attr = Descriptor()




class Person:
    def __init__(self, name):
        self._name = name


    class Name:
        "name descriptor docs"
        def __get__(self, instance, owner):
            print('fetch')
            return instance._name

        def __set__(self, instance, value):
            print('change...')
            instance._name = value

        def __delete__(self, instance):
            print('del...')
            del instance._name


    name = Name()

class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('can\'t get attribute')
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("cant't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

class Person1:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print("getname...")
        return self._name

    def setName(self, name):
        print("setName...")
        self._name = name
        return self._name

    def delName(self):
        print("del...")
        del self._name
        return 'del attr done'

    name = Property(getName, setName, delName)


def decora(a):
    print("***", a)
    print(a.__dict__)
    print(a.myfunc(2))
    return a

@decora
class testdec:
    def __init__(self, value):
        print("init", value)
        self.value = value

    @staticmethod
    def myfunc(val):
        return val**2
c = testdec(4)

# p = Person('Bob Smith')
# print(Person.Name.__doc__)
# print(p.name)
# p.name = '3'
# print(p.name)
# del p.name
#
# print(p.name)