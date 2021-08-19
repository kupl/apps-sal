import math
l = [0, 1, 2, 3, 4, 6, 9, 13]
s = 316
while l[-1] < 10 ** 9:
    l.append(math.floor(math.sqrt(s)) + 1)
    s += l[-1] ** 2
n = int(input())
while n > 0:
    n -= 1
    a = int(input())
    c = 0
    for i in l:
        if i <= a:
            c += 1
        else:
            break
    print(c - 1)
