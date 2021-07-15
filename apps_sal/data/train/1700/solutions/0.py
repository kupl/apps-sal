class DynamicConnectivity(object):
    par = []
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def union(self, p, q):
        if self.root(p) != self.root(q):
            self.par[self.root(p)] = q

    def root(self, p):
        pp = p
        while self.par[pp] != pp:
            pp = self.par[pp]
        return pp
        
    def connected(self, p, q):
        return True if self.root(p)==self.root(q) else False

