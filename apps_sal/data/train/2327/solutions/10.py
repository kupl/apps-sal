class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        self.el = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)


class BIT_Range():
    def __init__(self, n):
        self.n = n
        self.bit0 = BIT(n + 1)
        self.bit1 = BIT(n + 1)

    def add(self, l, r, x):
        l += 1
        self.bit0.add(l, -x * (l - 1))
        self.bit0.add(r + 1, x * r)
        self.bit1.add(l, x)
        self.bit1.add(r + 1, -x)

    def sum(self, i):
        if i == 0:
            return 0
        return self.bit0.sum(i) + self.bit1.sum(i) * i

    def get(self, i):
        return self.sum(i + 1) - self.sum(i)

    def get_range(self, i, j):
        return self.sum(j) - self.sum(i)


def main1(n, m, lr):
    lary = [[] for _ in range(m + 1)]
    for l, r in lr:
        lary[r - l + 1].append([l, r])
    ret = [n]
    bitr = BIT_Range(m + 1)
    cnt = 0
    for d in range(2, m + 1):
        for l, r in lary[d - 1]:
            cnt += 1
            bitr.add(l, r + 1, 1)
        tmp = n - cnt
        dd = d
        while dd <= m:
            tmp += bitr.get(dd)
            dd += d
        ret.append(tmp)
    return ret


def __starting_point():
    n, m = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(n)]
    print(*main1(n, m, lr), sep='\n')


__starting_point()
