import math


t = eval(input())
while t > 0:
    t = t - 1
    a = eval(input())
    s = 0
    s = 2 * (a + 1) + 2 * (a - 1)
    i = 0
    b = a + 1
    if a % 2 == 0:
        print(s)
    else:
        n = (a - 1) / 2 + 1
        if n % 2 == 0:
            print(a)
        else:
            print(a * 2)
