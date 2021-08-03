class DynamicConnectivity(object):
    def __init__(self, n):
        # class takes the number of objects n as input,
        # and initializes a data structure with objects numbered from
        # 0 to N-1
        self.clusters = {}

    def union(self, p, q):
        # union connects point p with point q
        pp = self.clusters.get(p, None)
        qq = self.clusters.get(q, None)
        if pp and qq:
            # merge qq into pp
            pp |= qq
            # redirect all qq mappings to pp
            for c in qq:
                self.clusters[c] = pp
        elif pp:
            # extend pp to include q
            self.clusters[p].add(q)
            self.clusters[q] = self.clusters[p]
        elif qq:
            # extend qq to include p
            self.clusters[q].add(p)
            self.clusters[p] = self.clusters[q]
        else:
            # Create new cluster
            pq = {p, q}
            self.clusters[p] = pq
            self.clusters[q] = pq

    def connected(self, p, q):
        # connected checks if point p is connected to point q and returns a boolean
        return q in self.clusters.get(p, {})
