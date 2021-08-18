from math import gcd


def rec_ans(cp, cg):
    nonlocal n, nl
    if cp == n and cg == 1:
        return 1
    elif cp == n:
        return 0
    elif cg == 1:
        return 2**(n - cp)
    elif (cp, cg) in mem:
        return mem[(cp, cg)]
    else:
        temp = rec_ans(cp + 1, gcd(cg, nl[cp])) + rec_ans(cp + 1, cg)
        mem[(cp, cg)] = temp
        return temp


for _ in range(int(input())):
    n = int(input())
    nl = [int(x) for x in input().split()]
    mem = {}
    ans = 0
    for i in range(n):
        ans += rec_ans(i + 1, nl[i])
    print(ans)
