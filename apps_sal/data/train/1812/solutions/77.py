from collections import Counter


class Node:
    def __init__(self, l, r, num, time, left=None, right=None):
        self.l = l
        self.r = r
        self.num = num
        self.time = time
        self.left = left
        self.right = right


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.t = self.build(0, len(arr) - 1)

    def build(self, l, r):
        if l == r:
            return Node(l, r, self.arr[l], 1)

        mid = (r + l) // 2
        num, time = -1, 0
        ln, rn = self.build(l, mid), self.build(mid + 1, r)
        for n in [ln, rn]:
            if n:
                if n.num == num:
                    time += n.time
                else:
                    if time > n.time:
                        time -= n.time
                    else:
                        num = n.num
                        time = n.time - time

        return Node(l, r, num, time, ln, rn)

    def trange(self, l, r, n):
        if l > r:
            return (-1, 0)

        if l == n.l and r == n.r:
            return (n.num, n.time)

        mid = (n.r + n.l) // 2
        if r < mid:
            return self.trange(l, r, n.left)
        elif l > mid:
            return self.trange(l, r, n.right)

        num, time = -1, 0
        for n, t in [self.trange(l, mid, n.left), self.trange(mid + 1, r, n.right)]:
            if n == num:
                time += t
            else:
                if time > t:
                    time -= t
                else:
                    num = n
                    time = t - time
        return num, time

    def query(self, left: int, right: int, threshold: int) -> int:
        x, _ = self.trange(left, right, self.t)
        if self.arr[left:right + 1].count(x) >= threshold:
            return x
        return -1
