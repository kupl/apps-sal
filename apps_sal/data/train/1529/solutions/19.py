import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = math.factorial(n)
    s = 0
    for i in range(n):
        s = s + a[i]
    s = s * (f // n)
    (r, i, k) = (0, 1, 1)
    while i <= n:
        r = r + k * s
        k = k * 10
        i = i + 1
    print(r)
