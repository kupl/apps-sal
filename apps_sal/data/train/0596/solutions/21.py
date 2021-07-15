import math
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    t = math.floor(k/2)
    r = n + t
    s = r*(r+1)
    if k % 2 == 1:
        s -= n
    else:
        s = s - r
        s = s - t
    if n == 0:
        k = k - 1 
        s = int(k*(k+1))
    print(s % 1000000007)

