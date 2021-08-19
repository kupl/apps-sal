class DynamicConnectivity(object):
    # class takes the number of objects n as input,
    # and initializes a data structure with objects numbered from
    # 0 to N-1
    def __init__(self, n):
        self.links = [[] for i in range(n)]

# union connects point p with point q
    def union(self, p, q):
        for [x, y] in [[p, q], [q, p]]:
            self.links[x].append(y)

# connected checks if point p is connected to point q and returns a boolean
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
