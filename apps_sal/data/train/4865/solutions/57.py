def multiply(*args):
    c = 1
    for i in args:
        c = c * i
    print(str(c))
    return c

multiply(2,4,3)
