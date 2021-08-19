# cook your dish here
import sys
input = sys.stdin.readline
t = int(input())
for you in range(t):
    n = int(input())
    poss = 0
    for i in range(1, n + 1):
        z = i
        y = n - i
        l = []
        op = []
        ok = 2
        while(ok * ok <= z):
            if(z % ok == 0):
                l.append(ok)
                while(z % ok == 0):
                    z = z // ok
            ok += 1
        if(z != 1):
            l.append(z)
        ok = 2
        while(ok * ok <= y):
            if(y % ok == 0):
                op.append(ok)
                while(y % ok == 0):
                    y = y // ok
            ok += 1
        if(y != 1):
            op.append(y)
        if(len(op) == 2 and op[0] * op[1] == n - i and len(l) == 2 and l[0] * l[1] == i):
            poss = 1
            break
    if(poss):
        print("YES")
    else:
        print("NO")
