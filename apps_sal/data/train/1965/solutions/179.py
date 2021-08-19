class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False, 0
        if self.size[x] > self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True, self.size[x]


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def getMST(whos):
            nonlocal edges, n
            unionfind = UnionFind(n)
            # mst=set()
            reqEdges = set()
            nodes = 0
            for indx, (typ, fnode, tnode) in enumerate(edges):
                # if fnode not in mst or tnode not in mst:
                siz = 0
                if typ == 3 or typ == whos:
                    res, siz = unionfind.union(fnode, tnode)
                    if res:
                        reqEdges.add(tuple(edges[indx]))
                        nodes = max(nodes, siz)
                if siz == n:
                    break
            return siz == n, reqEdges

        edges.sort(key=lambda item: -item[0])
        ares, alice = getMST(1)
        if not ares:
            return -1
        bres, bob = getMST(2)
        if not bres:
            return -1
        nset = alice.union(bob)
        return len(edges) - len(nset)
