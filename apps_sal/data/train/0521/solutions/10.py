from math import *
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    x, y = map(int, input().split())
    ans = 0
    for i in range(n // 2):
        a = l[i]
        b = l[n - i - 1]
        theta1 = (b - x) / y
        theta2 = (a - x) / y
        theta1 = atan(theta1)
        theta2 = atan(theta2)
        ans += (theta1 - theta2)
    print(abs(ans))
