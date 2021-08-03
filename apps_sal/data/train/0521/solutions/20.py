import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    p, q = list(map(int, input().split()))
    a = sorted(a)
    b = [0] * len(a)
    s = 0
    for i in range(len(a)):
        b[i] = a[i] - p
    for i in range(len(a) // 2):
        s = s - math.atan(b[i] / q) + math.atan(b[n - 1 - i] / q)
    print(s)
