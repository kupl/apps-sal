import sys
import heapq


class DynamicMedian:

    def __init__(self):
        self.l_q = []
        self.r_q = []
        self.l_sum = 0
        self.r_sum = 0

    def add(self, val):
        if len(self.l_q) == len(self.r_q):
            self.l_sum += val
            val = -heapq.heappushpop(self.l_q, -val)
            self.l_sum -= val
            heapq.heappush(self.r_q, val)
            self.r_sum += val
        else:
            self.r_sum += val
            val = heapq.heappushpop(self.r_q, val)
            self.r_sum -= val
            heapq.heappush(self.l_q, -val)
            self.l_sum += val

    def median_low(self):
        if len(self.l_q) + 1 == len(self.r_q):
            return self.r_q[0]
        else:
            return -self.l_q[0]

    def median_high(self):
        return self.r_q[0]

    def minimum_query(self):
        res1 = len(self.l_q) * self.median_high() - self.l_sum
        res2 = self.r_sum - len(self.r_q) * self.median_high()
        return res1 + res2


class BIT:

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        i = i + 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def sum(self, i, j):
        return self._sum(j) - self._sum(i)


input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
bit = BIT(n)
dm = DynamicMedian()
memo = {}
for i in range(n):
    memo[a[i] - 1] = i
b = [0] * n
for i in range(n):
    dm.add(memo[i])
    b[i] = dm.minimum_query() - (i + 1) ** 2 // 4
ans = [0] * n
tmp = 0
for i in range(len(a)):
    bit.add(memo[i], 1)
    tmp += bit.sum(memo[i] + 1, n)
    ans[i] = tmp + b[i]
print(*ans)
