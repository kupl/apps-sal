class DynamicConnectivity(object):
    def __init__(self, n):
        self.links = [[] for i in range(n)]

    def union(self, p, q):
        for [x, y] in [[p, q], [q, p]]:
            self.links[x].append(y)

    def connected(self, p, q):
        stack, seen = [p], set()
        while len(stack):
            p = stack.pop()
            if p == q:
                return True
            if p in seen:
                continue
            stack += self.links[p]
            seen.add(p)
        return False
