class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.x_idxs = x_idxs = defaultdict(list)
        for i, x in enumerate(arr):
            x_idxs[x].append(i)
        self.a = arr
        self.n = n = len(arr)
        self.tree = [-1] * (n * 4)
        self.build_tree(1, 0, n - 1)

    def build_tree(self, v, l, r):
        a, tree = self.a, self.tree
        if l == r:
            tree[v] = a[l]
            return
        mid = (l + r) // 2
        self.build_tree(2 * v, l, mid)
        self.build_tree(2 * v + 1, mid + 1, r)
        if tree[2 * v] != -1 and self.count(tree[2 * v], l, r) * 2 > r - l + 1:
            tree[v] = tree[2 * v]
        elif tree[2 * v + 1] != -1 and self.count(tree[2 * v + 1], l, r) * 2 > r - l + 1:
            tree[v] = tree[2 * v + 1]

    def count(self, x, l, r):
        f = bisect.bisect_right
        idxs = self.x_idxs[x]
        return f(idxs, r) - f(idxs, l - 1)

    def query_tree(self, v, l, r, queryl, queryr):
        tree = self.tree
        if queryr < l or r < queryl:
            return -1, -1
        if queryl <= l and r <= queryr:
            if tree[v] == -1:
                return -1, -1
            x = tree[v]
            xcount = self.count(x, queryl, queryr)
            return (x, xcount) if xcount * 2 > queryr - queryl + 1 else (-1, -1)
        mid = (l + r) // 2
        res_left = self.query_tree(2 * v, l, mid, queryl, queryr)
        if res_left[0] > -1:
            return res_left
        res_right = self.query_tree(2 * v + 1, mid + 1, r, queryl, queryr)
        if res_right[0] > -1:
            return res_right
        return -1, -1

    def query(self, left, right, threshold):
        res = self.query_tree(1, 0, self.n - 1, left, right)
        if res[1] >= threshold:
            return res[0]
        return -1
    

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

