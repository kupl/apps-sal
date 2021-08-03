"""
NTC here
"""
from sys import setcheckinterval, stdin
setcheckinterval(1000)

# print("Case #{}: {} {}".format(i, n + m, n * m))


def iin(): return int(stdin.readline())


def lin(): return list(map(int, stdin.readline().split()))


n = iin()
s = lin()
s.sort()
mix = s[0]
maxx = s[(n - 1)]
miy = s[n]
may = s[-1]
ans = (maxx - mix) * (may - miy)
for i in range(1, n):
    ans = min((s[-1] - s[0]) * (s[i + n - 1] - s[i]), ans)
print(ans)
