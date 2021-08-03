import math
t = int(input())
ans = list()
for i in range(t):
    n = list(map(int, input().split()))
    x = math.gcd(n[0], n[1])
    y = (n[0] / x) * (n[1] / x)
    ans.append(y)
for l in ans:
    print(int(l))
