from bisect import bisect_left
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    l = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ma = min(a)
    mb = min(b)

    ans = 0

    for j in range(l):
        temp = max(a[j] - ma, b[j] - mb)
        ans += temp

    print(ans)
