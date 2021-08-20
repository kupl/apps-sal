import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        diff = a[i] - a[i + 1]
        if diff <= 0:
            continue
        else:
            ans = max(len(bin(diff)) - 2, ans)
            a[i + 1] = a[i]
    print(ans)
