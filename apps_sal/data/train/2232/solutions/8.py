import sys
from fractions import gcd
import math


def lcm(x, y):
    return x * y // gcd(x, y)


def seive(lim):
    for x in range(2, lim + 1):
        if len(factors[x]) == 0:
            factors[x].append((x, 1))
            for y in range(x + x, lim + 1, x):
                yy = y
                cnt = 0
                while yy % x == 0:
                    cnt += 1
                    yy //= x
                factors[y].append((x, cnt))


factors = []
for i in range(10 ** 5 + 2):
    factors.append([])
seive(10 ** 5 + 1)
n = int(input())
curLvl = 1
curValue = 2
nxtLvl = 2
ans = ''
while curLvl <= n:
    f = factors[curLvl]
    x = 1
    for item in f:
        x *= item[0] ** (item[1] // 2 + item[1] % 2)
    x = lcm(x, nxtLvl)
    ans += str((x * x - curValue) // curLvl) + '\n'
    curValue = x
    curLvl += 1
    nxtLvl += 1
sys.stdout.write(ans)
