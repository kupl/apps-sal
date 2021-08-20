import sys
readline = sys.stdin.readline
read = sys.stdin.read
n = int(readline())
ans = 0
bmax = 1 << 31
same = 1
for i in range(n):
    (a, b) = map(int, readline().split())
    ans += a
    if a > b:
        bmax = min(b, bmax)
        same = 0
ans -= bmax
if same:
    ans = 0
print(ans)
