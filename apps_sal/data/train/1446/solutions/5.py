import math
t = int(input())
for _ in range(t):
    n = int(input())

    if n == 1:
        print(2)
        continue

    temp = math.floor(math.log(n + 1, 2))
    if 2**temp == n + 1:
        print((n + 1) // 2 - 1)
    else:
        print(-1)
