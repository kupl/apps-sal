try:
    from cp import input, setInputFile
except:
    pass
import math
import copy
import numpy as np
import sys
def input(): return sys.stdin.readline()
def itarr(arr): return list(range(len(arr)))
def mp(): return list(map(int, input().split()))
def lmp(): return list(map(int, input().split()))
def inp(): return int(input())


MOD = 1000000007


def mexp(m, p):
    if p == 1:
        return m % MOD
    x = (m % MOD * m % MOD) % MOD
    r = mexp(x % MOD, p // 2)
    if p % 2 == 0:
        return r % MOD
    else:
        return (m % MOD * r % MOD) % MOD


def main():
    n, b = mp()
    t = b % MOD
    g = (b * b) % MOD
    n %= MOD
    if n == 2:
        print(g)
        return
    if n == 1:
        print(t)
        return

    MI = np.matrix(np.array([[(b - 1) % MOD, (b - 1) % MOD], [1, 0]]))

    arr = mexp(MI, n - 2)
    arr = np.array(arr)
    ans = (arr[0][0] * g) % MOD + (arr[0][1] * t) % MOD
    ans %= MOD
    print(ans)


for _ in range(int(input())):
    main()
