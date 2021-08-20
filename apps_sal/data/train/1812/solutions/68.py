import collections


class StNode:

    def __init__(self, left, right):
        self.left = None
        self.right = None
        self.stats = None
        self.vals = (left, right)


class St:

    def __init__(self, arr):
        self.arr = arr
        self.root = self.build(0, len(arr) - 1)

    def build(self, i, j):
        if i == j:
            N = StNode(i, j)
            N.stats = collections.Counter([self.arr[i]])
            return N
        k = i + j >> 1
        N = StNode(i, j)
        N.left = self.build(i, k)
        N.right = self.build(k + 1, j)
        N.stats = N.left.stats + N.right.stats
        return N

    def retrieveLargestStats(self, i, j, t):
        R = self.root.stats.copy()
        abort = False

        def helper(node):
            nonlocal abort, R, i, j, t
            if abort:
                return
            if not R or max(R.values()) < t:
                abort = True
                R = dict()
                return
            (l, r) = node.vals
            if i > r or l > j:
                R -= node.stats
                return
            if i <= l and r <= j:
                return
            if l == r:
                return
            helper(node.left)
            helper(node.right)
        helper(self.root)
        if not R:
            return -1
        m = max(R, key=lambda x: R[x])
        return m if R[m] >= t else -1


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.ST = St(arr)

    def query(self, left: int, right: int, threshold: int) -> int:
        return self.ST.retrieveLargestStats(left, right, threshold)
