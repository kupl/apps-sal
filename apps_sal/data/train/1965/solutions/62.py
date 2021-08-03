class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent = {}
        for i in range(1, n + 1):
            parent[i] = i

        r = 0

        both = 0
        for c, a, b in edges:
            if c == 3:
                if self.find(a, parent) == self.find(b, parent):
                    r += 1
                else:
                    self.union(a, b, parent)
                    both += 1

        alice = both
        aliceP = parent.copy()
        for c, a, b in edges:
            if c == 1 or c == 3:
                if self.find(a, aliceP) == self.find(b, aliceP):
                    if c == 1:
                        r += 1
                else:
                    self.union(a, b, aliceP)
                    alice += 1
        print(alice)
        if alice < n - 1:
            return -1

        bob = both
        bobP = parent.copy()
        for c, a, b in edges:
            if c == 2 or c == 3:
                if self.find(a, bobP) == self.find(b, bobP):
                    if c == 2:
                        r += 1
                else:
                    self.union(a, b, bobP)
                    bob += 1
        print(bob)
        if bob < n - 1:
            return -1
        return r

    def union(self, a, b, parent):
        pa = self.find(a, parent)
        pb = self.find(b, parent)
        if pa == pb:
            return
        parent[pb] = pa
        return

    def find(self, a, parent):
        path = [a]
        while a in parent and parent[a] != a:
            a = parent[a]
            path.append(a)
        for p in path:
            parent[p] = a
        return a
