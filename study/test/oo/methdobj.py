
class mobj:
    def doit(self, message):
        print(message)


class eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1
        x(42)


class selfless:
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):
        return arg1+arg2

    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2

def square(arg):
    return arg ** 2

class sums:
    def __init__(self, val):
        self.val = val

    def __call__(self, args):
        return self.val + args


class product:
    def __init__(self, val):
        self.val = val

    def doit(self, arg):
        return self.val * arg


class Negate:
    def __init__(self, val):
        self.val = -val

    def __repr__(self):
        return 'Negate __repr__' + str(self.val)

    def __str__(self):
        return str(self.val)

    def __call__(self, arg):
        print('Negate.__call__', arg)


sobj = sums(2)
proobj = product(3)
actions = [square, sobj, proobj.doit, Negate]
tbl = {act(5): act for act in actions}
for (key, value) in tbl.items():
    print('{0} => {1}'.format(key, value))
