# 10 times faster than naive
class DynamicConnectivity(object):
    def __init__(self, n):
        self.items = {i: {i} for i in range(n)}

    def union(self, p, q):
        if self.items[p] is not self.items[q]:
            for x in self.items[q]:
                self.items[p].add(x)
                self.items[x] = self.items[p]

    def connected(self, p, q):
        return q in self.items[p]
