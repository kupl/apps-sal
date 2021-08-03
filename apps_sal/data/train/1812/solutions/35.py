class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.left_child = None
        self.right_child = None
        self.Maj_num = None
        self.Maj_f = 0


class MajorityChecker:
    def __init__(self, arr: List[int]):
        def create_Tree(i, j):
            cur = Node(i, j)
            if i == j:
                cur.Maj_num = arr[i]
                cur.Maj_f = 1
            else:
                m = (i + j) // 2
                cur.left_child, n1, f1 = create_Tree(i, m)
                cur.right_child, n2, f2 = create_Tree(m + 1, j)
                if n1 == n2:
                    cur.Maj_num = n1
                    cur.Maj_f = f1 + f2
                else:
                    if f1 >= f2:
                        cur.Maj_num = n1
                        cur.Maj_f = f1 - f2
                    else:
                        cur.Maj_num = n2
                        cur.Maj_f = f2 - f1
            return cur, cur.Maj_num, cur.Maj_f

        self.root = create_Tree(0, len(arr) - 1)[0]
        self.index = defaultdict(list)
        for i, num in enumerate(arr):
            self.index[num].append(i)

    def traverse(self, node, i, j):
        if i == node.left and j == node.right:
            return node.Maj_num, node.Maj_f
        m = (node.left + node.right) // 2

        if i > m:
            return self.traverse(node.right_child, i, j)
        if j <= m:
            return self.traverse(node.left_child, i, j)
        else:
            n1, f1 = self.traverse(node.left_child, i, m)
            n2, f2 = self.traverse(node.right_child, m + 1, j)
            if n1 == n2:
                return n1, f1 + f2
            else:
                if f1 >= f2:
                    return n1, f1 - f2
                else:
                    return n2, f2 - f1

    def query(self, left: int, right: int, threshold: int) -> int:
        candidate = self.traverse(self.root, left, right)[0]
        if threshold <= bisect.bisect_right(self.index[candidate], right) - bisect.bisect_left(self.index[candidate], left):
            return candidate
        else:
            return -1
