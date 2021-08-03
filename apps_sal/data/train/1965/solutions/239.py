class DSU:
    def __init__(self, size):
        self.indexes = {i: i for i in range(size)}
        self.sizes = {i: 1 for i in range(size)}
        self.com = size

    def root(self, i):
        node = i
        while i != self.indexes[i]:
            i = self.indexes[i]

        while node != i:
            nnode = self.indexes[node]
            self.indexes[node] = i
            node = nnode

        return i

    def unite(self, i, j):
        ri, rj = self.root(i), self.root(j)
        if ri == rj:
            return

        self.indexes[ri] = rj
        self.sizes[rj] += self.sizes[ri]
        self.com -= 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        alice = DSU(n)
        bob = DSU(n)

        ans = 0

        for t, u, v in edges:
            if t == 3:
                aru, arv = alice.root(u - 1), alice.root(v - 1)
                bru, brv = bob.root(u - 1), bob.root(v - 1)
                if aru == arv and bru == brv:
                    ans += 1
                else:
                    alice.unite(u - 1, v - 1)
                    bob.unite(u - 1, v - 1)

        for t, u, v in edges:
            if t == 1:
                ru, rv = alice.root(u - 1), alice.root(v - 1)
                if ru == rv:
                    ans += 1
                else:
                    alice.unite(u - 1, v - 1)

            elif t == 2:
                ru, rv = bob.root(u - 1), bob.root(v - 1)
                if ru == rv:
                    ans += 1
                else:
                    bob.unite(u - 1, v - 1)

        if alice.com != 1 or bob.com != 1:
            return -1

        return ans
