import math
(t, x) = map(int, input().strip().split())
for l in range(t):
    n = int(input())
    if n >= 0:
        a = int(math.sqrt(n))
        b = a * a
        d = n - b
        if d <= int(x / 100 * n):
            print('yes')
        else:
            print('no')
