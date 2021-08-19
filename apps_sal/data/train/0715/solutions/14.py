from string import ascii_uppercase as alp
import sys
input = sys.stdin.readline
(inp, ip) = (lambda: int(input()), lambda: [int(w) for w in input().split()])
dt = {}
for i in range(26):
    dt[alp[i]] = 27 - i
s = input().strip()
ans = 0
for i in s:
    ans += dt[i]
print(ans)
