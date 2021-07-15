from collections import defaultdict
N, M = list(map(int, input().split()))
section = [list(map(int, input().split())) for i in range(N)]

# 区間の大きさごとに分類
D = defaultdict(list)
for sec in section:
    D[sec[1] - sec[0] + 1].append(sec)


class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= (i & -i)
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += (i & -i)

    def reset(self):
        self.bit = [0] * (self.size + 1)


BIT = BinaryIndexedTree(M)
certainly = 0  # 確実に通るもの

for d in range(1, M + 1):
    for l, r in D[d - 1]:
        certainly += 1
        BIT.add(l, 1)
        BIT.add(r + 1, -1)

    ans = N - certainly
    for i in range(d, M + 1, d):
        ans += BIT.sum(i)
    print(ans)

