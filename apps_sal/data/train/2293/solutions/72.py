import sys
input = sys.stdin.readline
n = int(input())
alst = list(map(int, input().split()))
max_ = 0
dp = [[a, 0] for a in alst]
for i in range(n):
    for s in range(1 << n):
        if s >> i & 1:
            lst = dp[s] + dp[s - (1 << i)]
            lst.sort(reverse=True)
            dp[s] = lst[:2].copy()
for (a, b) in dp[1:]:
    max_ = max(max_, a + b)
    print(max_)
