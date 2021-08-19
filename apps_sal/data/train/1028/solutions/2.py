t = int(input())


def dig(a):
    c = 0
    i = a
    while i > 0:
        c = c + 1
        i = i // 10
    return c


def sums(a, b):
    s = 0
    i = a
    while i > 0:
        s = s + pow(i % 10, b)
        i = i // 10
    return s


for i in range(t):
    a = int(input())
    b = dig(a)
    if int(sums(a, b)) == a:
        print('FEELS GOOD')
    else:
        print('FEELS BAD')
