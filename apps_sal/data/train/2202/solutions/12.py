# 1208D
class segTree():
    def __init__(self, n):
        self.t = [0] * (n << 2)

    def update(self, node, l, r, index, value):
        if l == r:
            self.t[node] = value
            return
        mid = (l + r) >> 1
        if index <= mid:
            self.update(node * 2, l, mid, index, value)
        else:
            self.update(node * 2 + 1, mid + 1, r, index, value)
        self.t[node] = self.t[node * 2] + self.t[node * 2 + 1]

    def query(self, node, l, r, value):
        if l == r:
            return self.t[node]
        mid = (l + r) >> 1
        if self.t[node * 2] >= value:
            return self.query(node * 2, l, mid, value)
        return self.query(node * 2 + 1, mid + 1, r, value - self.t[node * 2])


def do():
    n = int(input())
    nums = [int(i) for i in input().split(" ")]
    res = [0] * n
    weightTree = segTree(n)
    for i in range(1, n + 1):
        weightTree.update(1, 1, n, i, i)
    # print(weightTree.t)
    for i in range(n - 1, -1, -1):
        res[i] = weightTree.query(1, 1, n, nums[i] + 1)
        weightTree.update(1, 1, n, res[i], 0)
    return " ".join([str(c) for c in res])


print(do())
