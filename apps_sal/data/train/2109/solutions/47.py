from math import sqrt

q = int(input())
for _ in range(q):
    a, b = list(map(int, input().split()))
    m = a * b
    s = int(sqrt(m))
    ans = 2 * s - 1
    if s * (s + 1) >= m:
        ans -= 1
    if s * s == m and a != b:
        ans -= 1
    print(ans)
