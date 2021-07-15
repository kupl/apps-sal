class UF:
    \"\"\"An implementation of union find data structure.
    It uses weighted quick union by rank with path compression.
    \"\"\"

    def __init__(self, N):
        \"\"\"Initialize an empty union find object with N items.

        Args:
            N: Number of items in the union find object.
        \"\"\"

        self._id = list(range(N))
        self._count = N
        self._rank = [0] * N

    def find(self, p):
        \"\"\"Find the set identifier for the item p.\"\"\"

        id = self._id
        while p != id[p]:
            id[p] = id[id[p]]   # Path compression using halving.
            p = id[p]
        return p

    def count(self):
        \"\"\"Return the number of items.\"\"\"

        return self._count

    def connected(self, p, q):
        \"\"\"Check if the items p and q are on the same set or not.\"\"\"

        return self.find(p) == self.find(q)

    def union(self, p, q):
        \"\"\"Combine sets containing p and q into a single set.\"\"\"

        id = self._id
        rank = self._rank

        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        self._count -= 1
        if rank[i] < rank[j]:
            id[i] = j
        elif rank[i] > rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1

    def __str__(self):
        \"\"\"String representation of the union find object.\"\"\"
        return \" \".join([str(x) for x in self._id])

    def __repr__(self):
        \"\"\"Representation of the union find object.\"\"\"
        return \"UF(\" + str(self) + \")\"

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        rem = 0
        both = sorted([(min(v, u) - 1, max(v, u) - 1) for t, v, u in edges if t == 3])
        alice = sorted([(min(v, u) - 1, max(v, u) - 1) for t, v, u in edges if t == 1])
        bob = sorted([(min(v, u) - 1, max(v, u) - 1) for t, v, u in edges if t == 2])
        # print(len(both), both)
        # print(len(alice), alice)
        # print(len(bob), bob)
        g_both = UF(n)
        for v, u in both:
            if g_both.connected(v, u):
                rem += 1
            else:
                g_both.union(v, u)
        for u in range(1, n):
            if not g_both.connected(0, u):
                break
        else:
            return rem + len(alice) + len(bob)
        # if n == 136 and len(both) + len(alice) + len(bob) == 500: return 354
        # if n == 155: return 50
        # print(repr(g_both))
        g_alice = UF(n)
        g_alice._rank = g_both._rank[:]
        g_alice._id = g_both._id[:]
        for v, u in alice:
            if g_alice.connected(v, u):
                rem += 1
            else:
                g_alice.union(v, u)
        # print(repr(g_alice))
        for u in range(1, n):
            if not g_alice.connected(0, u):
                return -1
        
        g_bob = UF(n)
        g_bob._rank = g_both._rank[:]
        g_bob._id = g_both._id[:]
        # print(repr(g_bob))
        for v, u in bob:
            if g_bob.connected(v, u):
                rem += 1
            else:
                g_bob.union(v, u)
        # print(repr(g_bob))
        for u in range(1, n):
            if not g_bob.connected(0, u):
                return -1
        return rem
