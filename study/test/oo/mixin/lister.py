class ListInstance:
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (self.__class__.__name__, # My class's name
                                                      id(self),                # My address
                                                      self.__attrnames())       # name = value list

    def __attrname(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result

    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == "__" and attr[-2:] == "__":
                result += '\nname %s=<>\n' % (attr)
            else:
                result += '\nname %s=%s\n' % (attr, getattr(self, attr))
        return result


class ListTree:
    def __str__(self):
        self.__visited = {}
        return 'Instance of {0}, address {1}\n {2}{3}>'.format(self.__class__.__name__,
                                                               id(self),
                                                               self.__attrnames(self, 0),
                                                               self.__listClass(self.__class__, 4))

    def __listClass(self, aclass, indent):
        dots = '.' * indent
        if aclass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above>\n'.format(
                dots,
                aclass.__name__,
                id(aclass)
            )
        else:
            self.__visited[aclass] = True
            genabove = (self.__listClass(c, indent+4) for c in aclass.__bases__)

            return '\n{0}<Class {1}, adress {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aclass.__name__,
                id(aclass),
                self.__attrnames(aclass, indent),
                ''.join(genabove),
                dots
            )

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}=<>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result


class Spam(ListTree):
    def __init__(self):
        self.data1 = 'food'

class Super1:
    def __init__(self):
        self.data1 = 'spam'

    def ham(self):
        pass


class Sub1(Super1, ListTree):
    def __init__(self):
        Super1.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):
        pass


def factory(aclass, *args):
    return aclass(*args)


class Spam2:
    def doit(self, message):
        print("Spam2.doit() ", message)


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job


class mylist(list):
    def __getitem__(self, item):
        print('(indexing %s at %s)' % (self, item))
        return list.__getitem__(self, item - 1)


class Set:
    def __init__(self, value = []):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if x not in res:
                res.append(x)
        return res

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[key]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return "Set:" + repr(self.data)


class Mylist222(list):
    def __getitem__(self, item):
        print('(indexing %s at %s' % (self, item))
        return list.__getitem__(self, item -1)


if __name__ == "__main__":
    print(list('abc'))
    x = Mylist222('abc')
    print(x)

    print(x[1])
    print(x[2])

    x.append('spam');print(x)
    x.reverse(); print(x)
    # print(list('abc'))
    # myli = mylist('efg')
    # print(myli)
    #
    # print(myli[1])
    # print(myli[2])
    #
    # myli.append('higj')
    # print(myli)
    #
    # myli.reverse()
    # print(myli)
    # obj1 = factory(Spam2)
    # obj2 = factory(Person, 'bob', 'develop')develop


    # x = Sub1()
    # print(x)

    # y = Spam()
    # print(y)
    #
    # z = Super1()
    # print(z)