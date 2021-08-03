class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        class UnionFind:
            def __init__(self, n):
                self.count = n  # Number of groups
                self.root = list(range(n))  # Root node of each element
                self.leaf = [1] * n  # Number of leaf elements

            def union(self, e1, e2):
                x, y = self.find(e1), self.find(e2)
                if x != y:
                    self.count -= 1
                    if self.leaf[x] > self.leaf[y]:
                        x, y = y, x
                    self.leaf[y] += self.leaf[x]
                    self.root[x] = y

            def find(self, el):
                if el == self.root[el]:
                    return el
                else:
                    return self.find(self.root[el])

        UFA = UnionFind(n)
        UFB = UnionFind(n)

        edges.sort(reverse=True)

        res = 0
        for t, a, b in edges:
            a, b = a - 1, b - 1
            if t == 3:
                if UFA.find(a) == UFA.find(b):
                    res += 1
                else:
                    UFA.union(a, b)
                    UFB.union(a, b)
            elif t == 2:
                if UFB.find(a) == UFB.find(b):
                    res += 1
                else:
                    UFB.union(a, b)
            elif t == 1:
                if UFA.find(a) == UFA.find(b):
                    res += 1
                else:
                    UFA.union(a, b)
            else:
                pass

        return res if UFA.count == 1 and UFB.count == 1 else -1
