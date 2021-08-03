import math as m
for _ in range(int(input())):
    d = int(input())
    p = d
    c = 0
    while(True):
        a = int(m.log2(d))
        c = c + 1
        d = d - 2**a
        if d == 1 or d == 0:
            if p % 2 == 0:
                c = c - 1
                print(c)
                break
            else:
                print(c)
                break
