# Created by: WeirdBugsButOkay
# 28-06-2020, 20:12:37

import math

def solve() :
    n = int(input())
    s = input()
    #n = len(s)
    bal = 0
    ans = 0
    for i in range (0, n) :
        if s[i] == '(' :
            bal += 1
        else :
            bal -= 1
            ans = max(ans, -bal)
    print(ans)

t = 1
t = int(input())
for _ in range (0, t) :
    solve()

