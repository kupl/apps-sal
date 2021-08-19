import math
(t, x) = map(int, input().strip().split())
for l in range(t):
    n = int(input())
    a = int(math.sqrt(n))
    b = a * a
    d = n - b
    if int(d) == int(x / 100 * n):
        print('yes')
    else:
        print('no')
