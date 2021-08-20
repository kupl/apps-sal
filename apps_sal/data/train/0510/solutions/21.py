import sys
input = sys.stdin.readline


class SegTree:

    def __init__(self, size, f=lambda x, y: x | y, e=0):
        self.size = 2 ** (size - 1).bit_length()
        self.e = e
        self.tree = [e] * (self.size * 2)
        self.f = f

    def init_tree(self, l):
        for i in range(len(l)):
            self.tree[i + self.size] = l[i]
        for i in range(self.size - 1, -1, -1):
            self.tree[i] = self.f(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, i, v):
        i += self.size
        self.tree[i] = v
        while i > 0:
            i >>= 1
            self.tree[i] = self.f(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lval = self.e
        rval = self.e
        while l < r:
            if l & 1:
                lval = self.f(lval, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                rval = self.f(rval, self.tree[r])
            l >>= 1
            r >>= 1
        return self.f(lval, rval)


def a2i(c):
    return 1 << ord(c) - ord('a')


def main():
    N = int(input())
    S = [a2i(s) for s in input().strip()]
    Q = int(input())
    tree = SegTree(N + 5)
    tree.init_tree(S)
    for _ in range(Q):
        (t, x, y) = input().split()
        if t == '1':
            x = int(x) - 1
            y = 1 << ord(y) - ord('a')
            tree.update(x, y)
        else:
            x = int(x) - 1
            y = int(y)
            tmp = tree.query(x, y)
            ans = 0
            while tmp > 0:
                ans += tmp & 1
                tmp >>= 1
            print(ans)


def __starting_point():
    main()


__starting_point()
