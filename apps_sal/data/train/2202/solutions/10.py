from operator import add


class Stree:
    def __init__(self, f, n, default, init_data):
        self.ln = 2**(n - 1).bit_length()
        self.data = [default] * (self.ln * 2)
        self.f = f
        for i, d in init_data.items():
            self.data[self.ln + i] = d
        for j in range(self.ln - 1, 0, -1):
            self.data[j] = f(self.data[j * 2], self.data[j * 2 + 1])

    def update(self, i, a):
        p = self.ln + i
        self.data[p] = a
        while p > 1:
            p = p // 2
            self.data[p] = self.f(self.data[p * 2], self.data[p * 2 + 1])

    def get(self, i, j):
        def _get(l, r, p):
            if i <= l and j >= r:
                return self.data[p]
            else:
                m = (l + r) // 2
                if j <= m:
                    return _get(l, m, p * 2)
                elif i >= m:
                    return _get(m, r, p * 2 + 1)
                else:
                    return self.f(_get(l, m, p * 2), _get(m, r, p * 2 + 1))
        return _get(0, self.ln, 1)

    def find_value(self, v):
        def _find_value(l, r, p, v):
            if r == l + 1:
                return l
            elif self.data[p * 2] <= v:
                return _find_value((l + r) // 2, r, p * 2 + 1, v - self.data[p * 2])
            else:
                return _find_value(l, (l + r) // 2, p * 2, v)
        return _find_value(0, self.ln, 1, v)


def main():
    n = int(input())
    sums = {i: i for i in range(n + 1)}
    stree = Stree(add, n + 1, 0, sums)
    ss = list(map(int, input().split()))
    ss.reverse()
    pp = []
    for s in ss:
        sval = stree.find_value(s)
        pp.append(sval)
        stree.update(sval, 0)
    print(*(reversed(pp)))


def __starting_point():
    main()


__starting_point()
