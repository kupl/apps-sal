"""
NTC here
"""
from sys import setcheckinterval, stdin
setcheckinterval(1000)


def iin(): return int(stdin.readline())


def lin(): return list(map(int, stdin.readline().split()))


n = iin()
s = lin()
s.sort()
mix = s[0]
maxx = s[(n - 1)]
miy = s[n]
may = s[-1]
dp = []
dp.append([maxx, mix, may, miy])
for i in range(1, n):
    dp.append([s[-1], s[0], s[i + n - 1], s[i]])
ans = (dp[0][0] - dp[0][1]) * (dp[0][2] - dp[0][3])
for i in dp:
    ans = min(ans, (i[0] - i[1]) * (i[2] - i[3]))
print(ans)
