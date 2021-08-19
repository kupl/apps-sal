class DynamicConnectivity(object):

    def __init__(self, n):
        self.clusters = {}

    def union(self, p, q):
        pp = self.clusters.get(p, None)
        qq = self.clusters.get(q, None)
        if pp and qq:
            pp |= qq
            for c in qq:
                self.clusters[c] = pp
        elif pp:
            self.clusters[p].add(q)
            self.clusters[q] = self.clusters[p]
        elif qq:
            self.clusters[q].add(p)
            self.clusters[p] = self.clusters[q]
        else:
            pq = {p, q}
            self.clusters[p] = pq
            self.clusters[q] = pq

    def connected(self, p, q):
        return q in self.clusters.get(p, {})
