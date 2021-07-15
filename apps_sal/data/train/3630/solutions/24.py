from operator import *
def arithmetic(a, b, operator):
    if operator=='add':
        return add(a,b)
    elif operator=='subtract':
        return sub(a,b)
    elif operator=='multiply':
        return mul(a,b)
    elif operator=='divide':
        return truediv(a,b)

