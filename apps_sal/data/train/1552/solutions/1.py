import sys
n = int(sys.stdin.readline())
for _ in range(n):
    (p1, p2, m) = list(map(int, sys.stdin.readline().split()))
    l = min(p1, p2)
    while m > 0 and l > 0:
        k = min(l, m)
        l -= k
        m -= 1
    q = min(p1, p2)
    print(p1 - q + l + p2 - q + l)
