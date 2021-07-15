fifth  = lambda i, x: x if i%5 else -x
third  = lambda i, x: x if i%3 else 3*x
square = lambda x   : x if x<0 else x*x

def calc(a):
    return sum(fifth(i, third(i, square(x))) for i,x in enumerate(a, 1))
