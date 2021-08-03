from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce, lru_cache  # @lru_cache(None)
from fractions import gcd
import sys
def input(): return sys.stdin.readline().rstrip()
def I(): return int(input())
def Is(): return (int(x) for x in input().split())
def LI(): return list(Is())
def TI(): return tuple(Is())
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def TIR(n): return [TI() for _ in range(n)]
def S(): return input()
def Ss(): return input().split()
def LS(): return list(S())
def SR(n): return [S() for _ in range(n)]
def SsR(n): return [Ss() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]


sys.setrecursionlimit(10**6)
MOD = 10**9 + 7
INF = 10**18
# ----------------------------------------------------------- #


class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):  # 1-index
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):  # 1-index
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    """
    # 使用例
    bit = BinaryIndexedTree(10)     # 要素数を与えてインスタンス化
    bit.add(2, 10)    # a2に10を加える
    bit.add(3, -6)    # a3に-6を加える
    print(bit.sum(6)) # a1～a6の合計を返す
    print(bit.sum(6) - bit.sum(3))  # a4～a6の合計を返す
    """


s = S()
n = len(s)
s_index = defaultdict(list)
for i, x in enumerate(s):
    s_index[x].append(i)

T = [0] * n  # sでi番目の文字は、最終的な回文でT[i]番目の文字となる
flag = False  # 奇数個の文字が前にあったかフラグ(奇数個の文字が2つ以上あってはならない)
AC = []  # 最終的な回文での前半Aと後半Cのペア
for x, index_list in s_index.items():
    count = len(index_list)
    if count % 2 == 1:
        if flag:
            print(-1)
            return
        else:
            flag = True
            mid = index_list[count // 2]
            T[mid] = n // 2  # 回文の中心(B)
    for i in range(count // 2):
        a = index_list[i]
        c = index_list[-i - 1]
        AC.append((a, c))

AC.sort(key=itemgetter(0))  # 前半(a)の順番でソート
for i, (a, c) in enumerate(AC):
    T[a] = i  # a == i
    T[c] = n - i - 1

BIT = BinaryIndexedTree(n)
inversion = 0
for i, t in enumerate(T):
    i += 1  # 1-indexに変換
    t += 1  # 1-indexに変換
    BIT.add(t, 1)
    inversion += i - BIT.sum(t)
print(inversion)
