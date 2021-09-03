'''
def baz(x,y):
    return 2*x+y


def add(x, y, c): c(x+y)
def mul(x, y, c): c(x*y)

def baz(x, y, c): mul(2, x, lambda v, y=y, c=c: add(v, y, c))
'''
def add(v, x, y):
    return v+x+y

print((lambda v, x=2, y=3: add(v,x,y))(1))

def yes(info, no):
    print(info)

def no():
    print("error")

class Foo:
    def __init__(self, info):
        self._info = info

    def check(self):
        if self._info == "test":
            return True
        else:
            return False

    def search(self, yes, no):
        if self.check():
            yes(self._info, no)
        else:
            no()

class Baz:
    def __init__(self, foo1, foo2):
        self.foo1 = foo1
        self.foo2 = foo2

    def search(self, yes, no):
        return self.foo1.search(
                    yes,
                    lambda self=self, yes=yes, no=no: self.foo2.search(yes, no)
                )

foo1 = Foo("testd")
foo2 = Foo("test")
b = Baz(foo1, foo2)
b.search(yes, no)
