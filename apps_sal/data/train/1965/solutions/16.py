class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        class UnionFind:
            def __init__(self, n):
                self.group = n
                self.rank = [1] * n
                self.root = list(range(n))

            def union(self, e1, e2):
                x = self.find(e1)
                y = self.find(e2)
                if x != y:
                    self.group -= 1
                    if self.rank[x] > self.rank[y]:
                        x, y = y, x
                    self.rank[y] += self.rank[x]
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

        return res if UFA.group == 1 and UFB.group == 1 else -1
