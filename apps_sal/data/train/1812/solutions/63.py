import random


class St:
    class Node:
        def __init__(self, vals):
            self.vals = vals
            self.stat = None
            self.left = None
            self.right = None

    def __init__(self, arr):
        self.arr = arr
        self.root = self.build(0, len(self.arr) - 1)

    def build(self, i, j):
        if i == j:
            N = St.Node((i, j))
            N.stat = collections.Counter([self.arr[i]])
            return N

        N = St.Node((i, j))
        k = (i + j) >> 1
        N.left = self.build(i, k)
        N.right = self.build(k + 1, j)

        N.stat = N.left.stat + N.right.stat

        return N

    def retriveStat(self, i, j, t):
        sentinel = False
        res = self.root.stat.copy()

        def helper(node):
            nonlocal i, j, t, res, sentinel
            if sentinel:
                res = dict()
                return
            if not res or max(res.values()) < t:
                res = dict()
                sentinel = True
                return

            l, r = node.vals

            if r < i or l > j:
                res -= node.stat
                return

            if i <= l and r <= j:
                return

            if l != r:
                helper(node.left)
                helper(node.right)

        helper(self.root)

        if not res:
            return -1

        m = max(res, key=lambda x: res[x])
        return m if res[m] >= t else -1


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.StO = St(arr)

    def query(self, left: int, right: int, threshold: int) -> int:
        return self.StO.retriveStat(left, right, threshold)
