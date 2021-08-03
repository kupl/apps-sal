class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        class Union:

            def __init__(self):

                self.parent = -1
                self.rank = 1

            def Find(self):

                if self.parent == -1:
                    return self
                return self.parent.Find()

            def UNION(self, node):

                L, R = self.Find(), node.Find()
                if L == R:
                    return 0
                elif L.rank > R.rank:
                    R.parent = L
                elif R.rank > L.rank:
                    L.parent = R
                else:
                    L.parent = R
                    R.rank += 1

                return 1

        alice, bob = [], []

        for t, u, v in edges:
            if t == 3:
                alice.append([t, u, v])
                bob.append([t, u, v])

        for t, u, v in edges:
            if t == 1:
                alice.append([t, u, v])
            elif t == 2:
                bob.append([t, u, v])

        Vertex = {}
        for i in range(n):
            Vertex[i + 1] = Union()

        Count, Common = 0, 0

        for t, u, v in alice:

            if Vertex[u].UNION(Vertex[v]) == 1:
                Count += 1
                if t == 3:
                    Common += 1

        if Count < n - 1:
            return -1

        for u in Vertex:
            Vertex[u].parent = -1

        Count = 0

        for t, u, v in bob:

            if Vertex[u].UNION(Vertex[v]) == 1:
                Count += 1

        if Count < n - 1:
            return -1

        return len(edges) - Common - 2 * (n - 1 - Common)
