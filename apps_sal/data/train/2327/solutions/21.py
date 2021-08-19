import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

# 内部で1-indexedに変えるので入力は0-indexedでよい
# i項目までの和（i含む）


class BitSum:
    def __init__(self, n):
        self.n = n + 3
        self.table = [0] * (self.n + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.table[i] += x
            i += i & -i

    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.table[i]
            i -= i & -i
        return res


def main():
    n, m = MI()
    dlr = []
    for _ in range(n):
        l, r = MI()
        dlr.append((r - l + 1, l, r + 1))
    dlr.sort()
    bit = BitSum(m + 1)
    i = 0
    for k in range(1, m + 1):
        while i < n and dlr[i][0] <= k:
            d, l, r = dlr[i]
            bit.add(l, 1)
            bit.add(r, -1)
            i += 1
        print(n - i + sum(bit.sum(a) for a in range(k, m + 1, k)))


main()
