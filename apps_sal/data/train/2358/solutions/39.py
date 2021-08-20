from struct import pack, unpack
import math
from heapq import heapify, heappush as hpush, heappop as hpop


class FibonacciHeap:

    def __init__(self, mm):
        self.inf = 1 << 100
        self.mm = mm
        self.roots = [[] for _ in range(mm)]
        self.min = self.inf
        self.minroot = None

    def add(self, v):
        nd = self.node(v)
        self.add_node(nd)
        return nd

    def add_node(self, nd):
        k = nd.order
        if nd.value < self.min:
            self.min = nd.value
            self.minroot = nd
        self.roots[k].append(nd)

    def setmin(self):
        mi = self.inf
        mirt = None
        for (i, rt) in enumerate(self.roots):
            while len(rt) >= 2:
                nd1 = rt.pop()
                nd2 = rt.pop()
                self.roots[i + 1].append(nd1.meld(nd2))
            if len(rt) and rt[0].value < mi:
                mi = rt[0].value
                mirt = rt[0]
        self.min = mi
        self.minroot = mirt
        return self.minroot

    def pop(self):
        nd = self.minroot
        mi = nd.value
        self.roots[nd.order].remove(nd)
        ch = nd.repChild
        if ch:
            nd = ch.right
            while 1:
                nnd = nd.right
                self.add_node(nd)
                l = nd.left
                r = nd.right
                if r != nd:
                    nd.right = nd
                    nd.left = nd
                    l.right = r
                    r.left = l
                nd.parent = None
                if nd == ch:
                    break
                nd = nnd
        self.setmin()
        return mi

    class node:

        def __init__(self, value):
            self.parent = None
            self.left = self
            self.right = self
            self.repChild = None
            self.order = 0
            self.marked = 0
            self.value = value

        def meld(self, other):
            if self.value > other.value:
                return other.meld(self)
            other.parent = self
            if not self.repChild:
                self.repChild = other
            else:
                l = self.repChild
                r = l.right
                l.right = other
                r.left = other
                other.left = l
                other.right = r
            self.order += 1
            return self

    def movetop(self, nd):
        p = nd.parent
        nd.marked = 0
        if not p:
            return nd
        l = nd.left
        r = nd.right
        if r != nd:
            p.repChild = r
            nd.right = nd
            nd.left = nd
            l.right = r
            r.left = l
        else:
            p.repChild = None
        nd.parent = None
        self.add_node(nd)
        if not p.parent:
            self.roots[p.order].remove(p)
            p.order -= 1
            self.add_node(p)

    def prioritize(self, nd, v):
        p = nd.parent
        nd.value = v
        if v < self.min:
            self.min = v
            self.minroot = nd
        if not p or p.value <= v:
            return nd
        self.movetop(nd)
        nn = p
        while nn.parent:
            if nn.marked == 0:
                nn.marked = 1
                break
            else:
                p = nn.parent
                self.movetop(nn)
                nn = p
        return nd

    def debug(self):

        def _debug(nd):
            if not nd:
                return ''
            s = str(nd.value) + ('(' + str(nd.left.value) + '-' + str(nd.right.value) + ')' if nd != nd.right else '')
            if nd.repChild:
                s += '[C=' + str(nd.repChild.value) + ']'
            if nd.parent:
                s += '[P=' + str(nd.parent.value) + ']'
            if not nd.repChild:
                return s
            ss = []
            ch = nd.repChild
            idch = id(ch)
            nd = ch.right
            while 1:
                ss.append(_debug(nd))
                if id(nd) == idch:
                    break
                nd = nd.right
            s += '[' + ', '.join(map(str, ss)) + ']'
            return s
        RE = []
        for (i, root) in enumerate(self.roots):
            for nd in root:
                if nd:
                    RE.append('<' + str(i) + '>' + _debug(nd))
        s = 'min=' + str(self.min) + ' '
        print(s + ' - '.join(map(str, RE)))


(xs, ys, xt, yt) = list(map(int, input().split()))
N = int(input())
X = [(xs, ys, 0), (xt, yt, 0)]
for _ in range(N):
    (x, y, r) = list(map(int, input().split()))
    X.append((x, y, r))
N += 2
DD = [[0] * N for _ in range(N)]
for i in range(N):
    (xi, yi, ri) = X[i]
    for j in range(N):
        (xj, yj, rj) = X[j]
        DD[i][j] = max(math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2) - (ri + rj), 0)
m = 1023


def dijkstra(n, E, i0=0):
    fb = FibonacciHeap(100)
    inf = unpack('q', pack('d', 10 ** 10 / 1))[0]
    D = [10 ** 10 / 1] * n
    done = [0] * n
    D[i0] = 0
    V = []
    for i in range(n):
        v = (unpack('q', pack('d', 0.0 if i == i0 else 10 ** 10 / 1))[0] | m) - (m - i)
        V.append(fb.add(v))
    while fb.minroot:
        di = fb.pop()
        (d, i) = (unpack('d', pack('q', (di | m) - m))[0], di & m)
        done[i] = 1
        for (j, w) in enumerate(DD[i]):
            if done[j] or j == i:
                continue
            nd = d + w
            if D[j] > nd:
                v = (unpack('q', pack('d', nd))[0] | m) - (m - j)
                fb.prioritize(V[j], v)
                D[j] = nd
    return D


print(dijkstra(N, X)[1])
