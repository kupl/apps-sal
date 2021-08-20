import math
T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = False
    am = min(a)
    bm = min(b)
    ans = 0
    for i in range(n):
        ans += max(a[i] - am, b[i] - bm)
    print(ans)
