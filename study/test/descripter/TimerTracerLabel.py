

def timer(label=''):
    def decorator(func):
        def onCall(*args):
            result = func(*args)
            print(label, result)
        return onCall
    return decorator

@timer('==>')
def listcomp(N):
    return [x * 2  for x in range(N)]


listcomp(5)
