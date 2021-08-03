import sys


class segmentTree:
    def __init__(self, n):
        self.n = n
        self.seg = [self.n + 1] * (self.n << 1)

    def update(self, p, value):
        p += self.n
        self.seg[p] = value
        while p > 1:
            p >>= 1
            self.seg[p] = min(self.seg[p * 2], self.seg[p * 2 + 1])

    def query(self, l, r):
        res = self.n
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = min(res, self.seg[l])
                l += 1
            if r & 1:
                res = min(res, self.seg[r - 1])
                r -= 1
            l >>= 1
            r >>= 1
        return res


inp = [int(x) for x in sys.stdin.read().split()]

n, m, q = inp[0], inp[1], inp[2]

p = [inp[idx] for idx in range(3, n + 3)]

index_arr = [0] * (n + 1)
for i in range(n):
    index_arr[p[i]] = i

a = [inp[idx] for idx in range(n + 3, n + 3 + m)]

leftmost_pos = [m] * (n + 1)
next = [-1] * m

for i in range(m - 1, -1, -1):
    index = index_arr[a[i]]
    right_index = 0 if index == n - 1 else index + 1
    right = p[right_index]
    next[i] = leftmost_pos[right]
    leftmost_pos[a[i]] = i

log = 0
while (1 << log) <= n:
    log += 1
log += 1
dp = [[m for _ in range(m + 1)] for _ in range(log)]

for i in range(m):
    dp[0][i] = next[i]

for j in range(1, log):
    for i in range(m):
        dp[j][i] = dp[j - 1][dp[j - 1][i]]

tree = segmentTree(m)
for i in range(m):
    p = i
    len = n - 1
    for j in range(log - 1, -1, -1):
        if (1 << j) <= len:
            p = dp[j][p]
            len -= (1 << j)
    tree.update(i, p)

inp_idx = n + m + 3
ans = []
for i in range(q):
    l, r = inp[inp_idx] - 1, inp[inp_idx + 1] - 1
    inp_idx += 2
    if tree.query(l, r + 1) <= r:
        ans.append('1')
    else:
        ans.append('0')
print(''.join(ans))
