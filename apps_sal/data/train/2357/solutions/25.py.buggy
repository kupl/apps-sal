import sys
from collections import deque
from copy import deepcopy
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from itertools import product, permutations, combinations, combinations_with_replacement
from functools import reduce
from math import gcd, sin, cos, tan, asin, acos, atan, degrees, radians

sys.setrecursionlimit(10**6)
INF = 10**20
eps = 1.0e-20
MOD = 10**9 + 7


def lcm(x, y):
    return x * y // gcd(x, y)


def lgcd(l):
    return reduce(gcd, l)


def llcm(l):
    return reduce(lcm, l)


def powmod(n, i, mod=MOD):
    return pow(n, mod - 1 + i, mod) if i < 0 else pow(n, i, mod)


def div2(x):
    return x.bit_length()


def div10(x):
    return len(str(x)) - (x == 0)


def intput():
    return int(input())


def mint():
    return map(int, input().split())


def lint():
    return list(map(int, input().split()))


def ilint():
    return int(input()), list(map(int, input().split()))


def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])


def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)


def ston(c, c0='a'):
    return ord(c) - ord(c0)


def ntos(x, c0='a'):
    return chr(x + ord(c0))


class counter(dict):
    def __init__(self, *args):
        super().__init__(args)

    def add(self, x, d=1):
        self.setdefault(x, 0)
        self[x] += d

    def list(self):
        l = []
        for k in self:
            l.extend([k] * self[k])
        return l


class comb():
    def __init__(self, n, mod=None):
        self.l = [1]
        self.n = n
        self.mod = mod

    def get(self, k):
        l, n, mod = self.l, self.n, self.mod
        if k < 0 or n < k:
            return 0
        k = n - k if k > n // 2 else k
        while len(l) <= k:
            i = len(l)
            l.append(l[i - 1] * (n + 1 - i) // i if mod == None else (l[i - 1] * (n + 1 - i) * powmod(i, -1, mod)) % mod)
        return l[k]


def pf(x, mode='counter'):
    C = counter()
    p = 2
    while x > 1:
        k = 0
        while x % p == 0:
            x //= p
            k += 1
        if k > 0:
            C.add(p, k)
        p = p + 2 - (p == 2) if p * p < x else x
    if mode == 'counter':
        return C
    S = set([1])
    for k in C:
        T = deepcopy(S)
        for x in T:
            for i in range(1, C[k] + 1):
                S.add(x * (k**i))
    if mode == 'set':
        return S
    if mode == 'list':
        return sorted(list(S))

######################################################


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7  # 出力の制限
N = 10**4
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

N, M = mint()
A = lint()
S = sum(A)
if S > M:
    print(0)
    return

n = S + N + M - S
k = S + N
mod = 10**9 + 7

# def modinv(x):
# xの逆元を求める際に[mod % x]の逆元が必要なので、関数の形でxの逆元を直接求めることは難しい。再帰を使えば行けそうだけど。

modinv_table = [-1] * (k + 1)
modinv_table[1] = 1
for i in range(2, k + 1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod


def binomial_coefficients(n, k):
    ans = 1
    for i in range(k):
        ans *= n - i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans


print(binomial_coefficients(n, k))
