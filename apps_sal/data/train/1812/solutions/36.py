from bisect import bisect, bisect_left


class Node():
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq


def merge(a, b):
    if a.val == b.val:
        return Node(a.val, a.freq + b.freq)
    if a.freq > b.freq:
        return Node(a.val, a.freq - b.freq)
    return Node(b.val, b.freq - a.freq)


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.arr = arr
        self.size = 1 << math.ceil(math.log(self.n, 2)) + 1
        self.tree = [None] * self.size
        self.indexes = {i: [] for i in self.arr}
        self.build(0, 0, self.n - 1)

    def build(self, pos, l, r):
        if l == r:
            self.tree[pos] = Node(self.arr[l], 1)
            self.indexes[self.arr[l]].append(l)
        else:
            mid = l + r >> 1
            self.build(pos * 2 + 1, l, mid)
            self.build(pos * 2 + 2, mid + 1, r)
            self.tree[pos] = merge(self.tree[pos * 2 + 1], self.tree[pos * 2 + 2])

    def pquery(self, pos, start, end, l, r):
        if l > end or r < start:
            return Node(0, 0)
        if start <= l and r <= end:
            return self.tree[pos]
        mid = l + r >> 1
        a = self.pquery(pos * 2 + 1, start, end, l, mid)
        b = self.pquery(pos * 2 + 2, start, end, mid + 1, r)
        return merge(a, b)

    def query(self, l: int, r: int, threshold: int) -> int:
        candidate = self.pquery(0, l, r, 0, self.n - 1).val
        if candidate == 0:
            return -1
        s = bisect_left(self.indexes[candidate], l)
        e = bisect(self.indexes[candidate], r)
        return candidate if e - s >= threshold else -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
