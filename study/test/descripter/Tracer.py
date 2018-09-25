

calls = 0

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        print("tracer __call__")
        # nonlocal calls
        # calls +=1
        self.calls += 1
        # global calls
        # calls += 1
        print('call %s to %s. \nBefore call it  i can do somethings.' % (self.calls, self.func.__name__))
        # print('call %s to %s. \nBefore call it  i can do somethings.' % (calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        return wrapper(self, instance)


class wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        print("wrapper __call__， \nself is %s, \ninstance is %s, \ndesc is %s" % (self.__dict__, self.subj, self.desc))
        return self.desc(self.subj, *args, **kwargs)


# def tracer(func):
#     # calls = 0
#     def wrapper(*args, **kwargs):
#         global calls
#         # nonlocal calls
#         calls += 1
#         print('call %s to %s. \nBefore call it  i can do somethings.' % (calls, func.__name__))
#         return func(*args, **kwargs)
#     return wrapper

@tracer
def spam(a, b, c):
    print("call spam")
    print(a*b*c)


class person:
    @tracer
    def giveRaise(self, percent):
        print("giveRaise's instance is : ", self.__dict__)
        print((1.0 + percent))


spam(1,1,2)
bob = person()
bob.giveRaise(.25)
