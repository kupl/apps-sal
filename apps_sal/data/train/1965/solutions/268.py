class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        self.father_alice = [i for i in range(n + 1)]
        self.father_bob = [i for i in range(n + 1)]
        res = 0
        edge_alice, edge_bob = 0, 0
        for type, u, v in edges:
            if type == 3:
                if self.connect(u, v, True) == 1:
                    edge_alice += 1
                    edge_bob += 1
                else:
                    res += 1

                self.connect(u, v, False)

        for type, u, v in edges:
            if type == 1:
                if self.connect(u, v, True) == 1:
                    edge_alice += 1
                else:
                    res += 1
            elif type == 2:
                if self.connect(u, v, False) == 1:
                    edge_bob += 1
                else:
                    res += 1

        if edge_alice == edge_bob == n - 1:
            return res
        return -1

    def find(self, x, is_alice):
        if is_alice:
            if self.father_alice[x] == x:
                return self.father_alice[x]
            self.father_alice[x] = self.find(self.father_alice[x], True)
            return self.father_alice[x]
        else:
            if self.father_bob[x] == x:
                return self.father_bob[x]
            self.father_bob[x] = self.find(self.father_bob[x], False)
            return self.father_bob[x]

    def connect(self, a, b, is_alice):
        if is_alice:
            root_a = self.find(a, True)
            root_b = self.find(b, True)
            if root_a == root_b:
                return 0
            else:
                self.father_alice[max(root_a, root_b)] = min(root_a, root_b)
                return 1
        else:
            root_a = self.find(a, False)
            root_b = self.find(b, False)
            if root_a == root_b:
                return 0
            else:
                self.father_bob[max(root_a, root_b)] = min(root_a, root_b)
                return 1
