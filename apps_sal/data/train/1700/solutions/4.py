import collections


class DynamicConnectivity(object):
    def __init__(self, n):
        self.map = collections.defaultdict(list)

    def union(self, p, q):
        self.map[p].append(q)
        self.map[q].append(p)

    def connected(self, p, q):
        handled = set()
        elements = set([p])
        while elements and not q in elements:
            elements = set(n for e in elements for n in self.map[e]).difference(handled)
            handled.update(elements)
        return q in elements
