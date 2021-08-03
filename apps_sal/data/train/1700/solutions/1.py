class DynamicConnectivity:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, p):
        stk = [p]
        rp = self.parents[stk[-1]]
        while rp != stk[-1]:
            stk.append(rp)
            rp = self.parents[rp]
        for i in stk:
            self.parents[i] = rp
        return rp

    def union(self, p, q):
        rp, rq = self.find(p), self.find(q)
        if rp == rq:
            return
        self.parents[rp] = rq

    def connected(self, p, q):
        return self.find(p) == self.find(q)
