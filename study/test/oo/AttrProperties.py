

class Person:
    def __init__(self, name):
        self._name = name


    def getName(self):
        print('__getName__')
        return self._name

    def setName(self, name):
        print('__setName__')
        self._name = name

    def delName(self):
        print('remove...')
        del self._name

    # name = property(getName, setName, delName, "name property docs")


    def testattr(self, names):
        print("exec name3 = ", names)

    testattr = property(testattr)

    @property
    def injectattr(self):
        "name property docs"
        print('fecth....')





bob = Person('Bob smith')
bob.injectattr
# print(bob.name)
# bob.name = 'Robert Smith'
# print(bob.name)
# del bob.name
#
# print('-'*20)
# sue = Person('Sue Jones')
# print(sue.name)
# print(Person.name.__doc__)

