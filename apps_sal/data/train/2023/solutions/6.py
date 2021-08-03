import math
n = int(input())
if n <= 3:
    for i in range(1, n + 1):
        print(i, end=' ')
    return

start = int(math.sqrt(n))
sqrtVal = start
already = [False] * 100005

if True:
    while start <= n:
        for i in range(sqrtVal):
            if already[start - i]:
                return
            print(start - i, end=' ')
            already[start - i] = True
        start += sqrtVal
        start = min(start, n)
