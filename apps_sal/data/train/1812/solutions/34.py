class Node:
    def __init__(self, left, right):
        self.i = left
        self.j = right
        self.left = None
        self.right = None
        self.Maj = None
        self.Maj_f = 0


class MajorityChecker:
    def __init__(self, arr: List[int]):
        def DFS(i, j):
            node = Node(i, j)
            if i == j:
                node.Maj = arr[i]
                node.Maj_f = 1
            else:
                m = (i + j) // 2
                node.left, a, b = DFS(i, m)
                node.right, c, d = DFS(m + 1, j)
                if a == c:
                    node.Maj = a
                    node.Maj_f = b + d
                elif b > d:
                    node.Maj = a
                    node.Maj_f = b - d
                else:
                    node.Maj = c
                    node.Maj_f = d - b
            return node, node.Maj, node.Maj_f

        self.root = DFS(0, len(arr) - 1)[0]
        self.index = defaultdict(list)
        for i, num in enumerate(arr):
            self.index[num].append(i)

    def DFS(self, node, l, r):
        if node.i == l and node.j == r:
            return node.Maj, node.Maj_f
        m = (node.i + node.j) // 2
        if l > m:
            return self.DFS(node.right, l, r)
        elif r < m + 1:
            return self.DFS(node.left, l, r)
        else:
            a, b = self.DFS(node.left, l, m)
            c, d = self.DFS(node.right, m + 1, r)
            if a == c:
                return a, b + d
            elif b > d:
                return a, b - d
            else:
                return c, d - b

    def query(self, left: int, right: int, threshold: int) -> int:

        candidate = self.DFS(self.root, left, right)[0]
        if threshold <= bisect.bisect_right(self.index[candidate], right) - bisect.bisect_left(self.index[candidate], left):
            return candidate
        else:
            return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
