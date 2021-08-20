class DynamicConnectivity(object):

    def __init__(self, n):
        self.a = [{i} for i in range(n)]

    def union(self, p, q):
        self.a[p] |= self.a[q]
        for i in self.a[q]:
            self.a[i] = self.a[p]

    def connected(self, p, q):
        return p in self.a[q]
