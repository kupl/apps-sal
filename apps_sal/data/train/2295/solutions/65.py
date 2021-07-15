import sys, math

input = sys.stdin.readline
N = int(input())
min_d = math.inf
sum_A = 0
for _ in range(N):
    a, b = list(map(int, input().split()))
    sum_A += a
    if a>b:
        min_d = min(min_d, b)
ans = max(0, sum_A-min_d)
print(ans)

