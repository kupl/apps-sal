import sys
from bisect import *


class Doubling:
    def __init__(self, A, K_max, decrement=True):
        """
        :param A: 写像 A:i->j を定義
        :param K_max: K_max = 2**(k_max) まで参照する可能性がある
        :param decrement: True = A の要素の decrement が必要
        """
        self.k_max = K_max.bit_length()
        self.n = len(A)
        self.decrement = decrement
        self.doubling = [[-1] * self.n for _ in range(self.k_max)]
        for i, a in enumerate(A):
            self.doubling[0][i] = a - self.decrement

        for i in range(1, self.k_max):
            for k in range(self.n):
                if self.doubling[i - 1][k] != -1:
                    self.doubling[i][k] = self.doubling[i - 1][self.doubling[i - 1][k]]

    def apply(self, start, K):
        """
        :param start: スタート地点
        :param K: K回進む
        :return:
        """
        i = start - self.decrement
        for k in range(K.bit_length()):
            m = 1 << k
            if m & K:
                i = self.doubling[k][i]
            if i is None:
                break
        return i + self.decrement


def binary_search_int(ok, ng, test, a, b):
    """
    :param ok: solve(x) = True を必ず満たす点
    :param ng: solve(x) = False を必ず満たす点
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if test(mid, a, b):
            ok = mid
        else:
            ng = mid
    return ok


input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
L = int(input())
Q = int(input())

A = []
for x in X:
    i = bisect_left(X, x + 1 + L)
    A.append(i - 1)
doubling = Doubling(A, N + 1, decrement=False)


def test(x, a, b):
    return X[doubling.apply(a, x)] < X[b]


for _ in range(Q):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if a > b:
        a, b = b, a
    print(binary_search_int(0, N, test, a, b) + 1)
