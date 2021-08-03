class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        i += 1

        while i <= self.n:
            self.bit[i] = max(self.bit[i], x)
            i += i & (-i)

    def acc(self, i):
        s = 0

        while i > 0:
            s = max(s, self.bit[i])
            i -= i & (-i)

        return s


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        l = startTime + endTime
        l = list(set(l))
        l.sort()
        idx = defaultdict(int)

        for i in range(len(l)):
            idx[l[i]] = i

        sep = [(idx[s], idx[e], p) for s, e, p in zip(startTime, endTime, profit)]
        sep.sort()
        bit = BIT(10**5 + 10)

        for s, e, p in sep:
            bit.add(e, bit.acc(s + 1) + p)

        return bit.acc(10**5 + 10)
