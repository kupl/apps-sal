class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        type_1, type_2, type_3 = [], [], []
        for type, a, b in edges:
            if type == 3:
                type_3.append((a, b))
            elif type == 1:
                type_1.append((a,b))
            elif type == 2:
                type_2.append((a, b))
        answer = 0
        b_u = None
        def helper(edges, u=None):
            nonlocal b_u
            u = Union(n, u)
            nonlocal answer
            for a, b in edges:
                if not u.union(a, b):
                    answer += 1
            b_u = u.backup()
            if not u.isConnected():
                return False
            return True
        helper(type_3)
        bb_u = copy.deepcopy(b_u)
        if not helper(type_1, copy.deepcopy(bb_u)):
            return -1
        if not helper(type_2, copy.deepcopy(bb_u)):
            return -1
        return answer


class Union:
    def __init__(self, n, p=None):
        self.n = n
        self.p = p if p else {i: i for i in range(1, n+1)}

    def backup(self):
        return self.p

    def union(self, p_a, b):
        a = p_a
        while self.p[a] != a:
            a = self.p[a]
        while self.p[b] != b:
            b = self.p[b]
        self.p[p_a] = a
        if a == b:
            return False
        else:
            self.p[b] = a
            return True

    def isConnected(self):
        return sum(i == self.p[i] for i in range(1, self.n+1)) == 1
