import sys
input = sys.stdin.readline
N = int(input())
res = 0
t = float("inf")
c = 0
for _ in range(N):
    x, y = map(int, input().split())
    if x > y:
        t = min(y, t)
    if x == y:
        c += 1
    res += x
if c == N:
    print(0)
    return
print(res - t)
