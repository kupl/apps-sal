import sys


def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


class Node:
    def __init__(self, val):
        self.val = val
        self.par = None


def solve():
    s = [x == "1" for x in ins()]
    n = len(s)
    if s[-1]:
        return print(-1)
    for i in range(n - 1):
        if s[i] != s[n - 2 - i]:
            return print(-1)
    if not s[0]:
        return print(-1)

    h = (n + 1) // 2
    nodes = [Node(i) for i in range(n)]
    for i in range(1, n):
        nodes[i].par = nodes[i - 1]

    i = 1
    while i + 2 < n:
        if s[i]:
            i += 1
            continue
        nodes[i + 2].par = nodes[i]
        nodes[i], nodes[i + 1] = nodes[i + 1], nodes[i]
        i += 1

    edges = set()
    for i in range(1, n):
        u = nodes[i].val
        v = nodes[i].par.val
        edges.add((min(u, v) + 1, max(u, v) + 1))
    for u, v in edges:
        print(u, v)


solve()
