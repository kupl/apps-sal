import math


def ispoweroftwo(y):
    return math.ceil(math.log(y, 2)) == math.floor(math.log(y, 2))


t = int(input())
for i in range(t):
    n = int(input())
    a = []
    if ispoweroftwo(n) and n != 1:
        print(-1, end=' ')
    if n == 1:
        print(1)
    if n >= 3 and (not ispoweroftwo(n)):
        a.append(2)
        a.append(3)
        a.append(1)
    if n > 3 and (not ispoweroftwo(n)):
        i = 4
        while i <= n:
            if ispoweroftwo(i):
                a.append(i + 1)
                a.append(i)
                i += 2
            else:
                a.append(i)
                i += 1
    print(*a)
