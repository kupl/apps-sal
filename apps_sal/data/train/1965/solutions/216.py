class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufAli = uf(n)
        ufBob = uf(n)

#         10 -> 2
        for edg in edges:
            x, y = edg[1], edg[2]
            if edg[0] == 1:
                ufAli.addEdge(x, y, 10)
            elif edg[0] == 2:
                ufBob.addEdge(x, y, 10)
            else:
                ufAli.addEdge(x, y, 1)
                ufBob.addEdge(x, y, 1)

        # print(ufAli.g, ufAli.kruskalmst())
        # print(ufBob.g, ufBob.kruskalmst())

        blueremoved = set()
        aliremoved = set()
        bobremoved = set()

        ans1 = ufAli.kruskalmst(blueremoved, aliremoved)
        ans2 = ufBob.kruskalmst(blueremoved, bobremoved)
        if ans1 == -1 or ans2 == -1:
            return -1

        # return ans1 + ans2
        return len(blueremoved) + len(aliremoved) + len(bobremoved)


class uf:
    def __init__(self, n):
        self.n = n
        self.g = []
        self.joinednodes = set()
        # self.totalnodes = set()

    def addEdge(self, x, y, cost):
        self.g.append((x, y, cost))
        # self.joinednodes

    def find(self, x, parent):
        if parent[x] == x:
            return x

        return self.find(parent[x], parent)

    def union(self, x, y, parent, rank):
        xroot, yroot = self.find(x, parent), self.find(y, parent)

        if xroot != yroot:
            if rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            elif rank[yroot] > rank[xroot]:
                parent[xroot] = yroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

    def kruskalmst(self, blue, rorg):
        # parent = { for edge in g}
        parent = {}
        rank = {}
        for edge in self.g:
            parent[edge[0]] = edge[0]
            parent[edge[1]] = edge[1]
            rank[edge[0]] = 0
            rank[edge[1]] = 0

        # print(parent, rank)
        success = 0
        self.g.sort(key=lambda edge: edge[2])
        for edge in self.g:
            x, y, cos = edge
            xroot = self.find(x, parent)
            yroot = self.find(y, parent)
            if xroot != yroot:
                success += 1
                self.union(xroot, yroot, parent, rank)

            else:
                if cos == 1:
                    blue.add((x, y))
                else:
                    rorg.add((x, y))

        if success == self.n - 1:

            # return success
            return len(self.g) - success

        return -1
