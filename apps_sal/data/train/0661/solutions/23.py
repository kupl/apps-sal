import math
(t, x) = map(int, input().split())
for i in range(t):
    n = int(input())
    m = math.sqrt(n)
    m = m // 1
    if n - m * m <= x * n / 100:
        print('yes')
    else:
        print('no')
