def pow(x, y):
    return x ** y


printPow = compose(print, pow)
lambda *x: print(pow(*x))
printPow(2, 3)
print(pow(*[2, 3]))
print(pow(2, 3))
