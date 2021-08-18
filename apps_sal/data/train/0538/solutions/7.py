import math
t = int(input())
for i in range(t):
    s, sg, fg, d, t = map(int, input().split())
    tot = (d * 50 * 3.6) / t
    final = s + tot
    a = abs(final - sg)
    b = abs(final - fg)
    if(a < b):
        print("SEBI")
    elif(b < a):
        print("FATHER")
    else:
        print("DRAW")
