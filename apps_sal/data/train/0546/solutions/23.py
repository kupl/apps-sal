import math
for _ in range(int(input())):
    d = int(input())
    c = 0
    while d > 0:
        n = math.floor(math.log2(d))
        x = pow(2, n)
        d -= x
        c += 1
    print(c - 1)
