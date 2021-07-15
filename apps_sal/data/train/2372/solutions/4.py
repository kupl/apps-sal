# Created by: WeirdBugsButOkay
# 28-09-2020, 13:44:16

import math

def ceil(a, b) :
    return (a + b - 1) // b

def calc(n, a) :
    return (a - 1 + ceil(n - a, a))

def solve() :
    n = int(input())
    i = int(math.sqrt(n))
    ans = n - 1
    ans = min(ans, calc(n, i))
    ans = min(ans, calc(n, i + 1))
    print(ans)

t = 1
t = int(input())
for _ in range (0, t) :
    solve()

