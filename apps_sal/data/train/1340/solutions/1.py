def count(a):
    x = 0
    for i in a:
        if i > 0:
            x = x + 1
    return x


for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    su = 0
    c = []
    d = []
    for i in a:
        if i > 0:
            su = su + i
    if su == 0:
        print(0)
        print(0)
    else:
        y = count(a)
        for i in range(len(a)):
            if i + 1 <= y:
                if a[i] < 0:
                    c.append(i + 1)
            elif a[i] > 0:
                d.append(i + 1)
        for i in range(abs(len(d) - len(c))):
            d.pop(0)
        print(su)
        print(len(c + d), *c + d, end=' ')
