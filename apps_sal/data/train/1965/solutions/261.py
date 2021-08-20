class DS:

    def __init__(self, n):
        self.par = list(range(n))

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        self.par[px] = py


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ga = defaultdict(set)
        gb = defaultdict(set)
        gc = defaultdict(set)
        count_a = 0
        count_b = 0
        count_c = 0
        for (t, u, v) in edges:
            u = u - 1
            v = v - 1
            if t == 1:
                ga[u].add(v)
                ga[v].add(u)
                count_a += 1
            if t == 2:
                gb[u].add(v)
                gb[v].add(u)
                count_b += 1
            if t == 3:
                gc[u].add(v)
                gc[v].add(u)
                count_c += 1
        ans = 0
        ds = DS(n)
        for u in gc:
            for v in gc[u]:
                ds.union(u, v)
        counter = Counter((ds.find(i) for i in range(n)))
        edge_num_type_3 = sum((val - 1 for val in list(counter.values())))
        ans += count_c - edge_num_type_3
        dsa = copy.deepcopy(ds)
        for u in ga:
            for v in ga[u]:
                dsa.union(u, v)
        if len(set((dsa.find(i) for i in range(n)))) > 1:
            return -1
        ans += count_a - (n - 1 - edge_num_type_3)
        dsb = copy.deepcopy(ds)
        for u in gb:
            for v in gb[u]:
                dsb.union(u, v)
        if len(set((dsb.find(i) for i in range(n)))) > 1:
            return -1
        ans += count_b - (n - 1 - edge_num_type_3)
        return ans
