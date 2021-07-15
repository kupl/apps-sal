from collections import deque
import sys
input = sys.stdin.readline

class FenwickTree:
    def __init__(self, size):
        self.data = [0] * (size + 1)
        self.size = size

    # i is exclusive
    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.data[i] += x
            i += i & -i

    def lower_bound(self, x):
        if x <= 0:
            return 0
        k = 1
        while k * 2 <= self.size:
            k *= 2
        i = 0
        while k > 0:
            if i + k <= self.size and self.data[i + k] < x:
                x -= self.data[i + k]
                i += k
            k //= 2
        return i


class RangeFenwickTree:
    def __init__(self, size):
        self.bit0 = FenwickTree(size)
        self.bit1 = FenwickTree(size)

    # i is exclusive
    def prefix_sum(self, i):
        return self.bit0.prefix_sum(i) * (i - 1) + self.bit1.prefix_sum(i)

    def add(self, l, r, x):
        self.bit0.add(l, x)
        self.bit0.add(r, -x)
        self.bit1.add(l, -x * (l - 1))
        self.bit1.add(r, x * (r - 1))


class FenwickTree2D:
    def __init__(self, H, W):
        self.H = H
        self.W = W
        self.data = [[0] * (H + 1) for _ in range(W + 1)]

    def add(self, a, b, x):
        a += 1
        b += 1
        i = a
        while i <= self.H:
            j = b
            while j <= self.W:
                self.data[i][j] += x
                j += j & -j
            i += i & -i

    def sum(self, a, b):
        a += 1
        b += 1
        ret = 0
        i = a
        while i > 0:
            j = b
            while j > 0:
                ret += self.data[i][j]
                j -= j & -j
            i -= i & -i
        return ret

S = list(map(lambda c: ord(c) - ord('a'), input().rstrip()))
N = len(S)
idx = [deque() for _ in range(26)]
for i, c in enumerate(S):
    idx[c].append(i)
if sum(len(v) % 2 for v in idx) > 1:
    print(-1)
    return
fw = FenwickTree(N + 1)
for i in range(1, N + 1):
    fw.add(i, 1)
ans = 0
for i in range(N // 2):
    min_cost = float('inf')
    char = -1
    for c in range(26):
        if len(idx[c]) <= 1:
            continue
        l = idx[c][0]
        cost = fw.prefix_sum(l + 1) - i
        r = idx[c][-1]
        cost += N - i - 1 - fw.prefix_sum(r + 1)
        if cost < min_cost:
            min_cost = cost
            char = c
    ans += min_cost
    fw.add(0, 1)
    fw.add(idx[char].popleft(), -1)
    fw.add(idx[char].pop(), -1)
print(ans)
