
import pickle

import test.impmoudle.import1 as imp1

filename = 'klass'
def save():
    obj = imp1.TestImp1()
    file = open(filename, 'wb')
    pickle.dump(obj, file)


def read():
    file = open(filename, 'rb')
    obj = pickle.load(file)
    obj.printer()


save()
read()