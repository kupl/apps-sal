import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    r = [0] * n
    for i in range(n):
        r[a[i] - 1] = i
    b = list(map(int, input().split()))
    d = [0] * n
    for i in range(k):
        d[b[i] - 1] = 1
    cnt = 0
    for i in range(k):
        idx = r[b[i] - 1]
        t = 0
        if idx > 0 and d[a[idx - 1] - 1] == 0:
            t += 1
        if idx < n - 1 and d[a[idx + 1] - 1] == 0:
            t += 1
        if t == 0:
            print(0)
            break
        elif t == 2:
            cnt += 1
        d[b[i] - 1] = 0
    else:
        print(pow(2, cnt, 998244353))
