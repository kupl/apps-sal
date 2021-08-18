import math
t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    while(n):
        t = int(math.sqrt(n))
        c += 1
        n = n - (t**2)
    print(c)
