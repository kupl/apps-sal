import math
t = int(input())
for x in range(t):
    (n, k) = map(int, input().split())
    tot = k - 1
    if n < k:
        left = k - n
        extra = n - 1
        if left <= extra:
            tot += left
        else:
            y = math.ceil(left / extra)
            tot = tot + (y * left - y * (y - 1) * extra // 2)
    print(tot % 1000000007)
