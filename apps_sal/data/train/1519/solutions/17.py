import math
for _ in range(int(input())):
    n = int(input())
    r = math.log2(n)
    if r != int(r):
        r = int(r)
        r = pow(2, r + 1)
    else:
        r = int(r)
        r = pow(2, r)
    print(r)
