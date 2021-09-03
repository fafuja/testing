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
