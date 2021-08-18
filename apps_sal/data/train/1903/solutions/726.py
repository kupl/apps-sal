class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges = []
        nodes = set()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dis, i, j))
                nodes.add(i)
                nodes.add(j)

        class UnionFindSet:
            def __init__(self, nodes):
                self._parents = {}
                self._ranks = {}
                for n in nodes:
                    self._parents[n] = n
                    self._ranks[n] = 1

            def find(self, u):
                while u != self._parents[u]:
                    self._parents[u] = self.find(self._parents[u])
                    u = self._parents[u]
                return u

            def union(self, u, v):
                pu, pv = self.find(u), self.find(v)
                if pu == pv:
                    return False

                if self._ranks[pu] < self._ranks[pv]:
                    self._parents[pu] = pv
                elif self._ranks[pu] > self._ranks[pv]:
                    self._parents[pv] = pu
                else:
                    self._parents[pv] = pu
                    self._ranks[pu] += 1

                return True

        uf = UnionFindSet(nodes)

        edges.sort()
        cost = 0
        for dis, u, v in edges:
            pu, pv = uf.find(u), uf.find(v)
            if pu == pv:
                continue
            else:
                cost += dis
                uf.union(u, v)

        return cost
