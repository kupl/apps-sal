import sys


class BIT():
    def __init__(self, n):
        self.BIT = [0] * (n + 1)
        self.num = n

    def query(self, idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx & (-idx)
        return res_sum

    # Ai += x O(logN)
    def update(self, idx, x):
        while idx <= self.num:
            self.BIT[idx] += x
            idx += idx & (-idx)
        return


input = sys.stdin.readline

N, M = map(int, input().split())
q = {i: [] for i in range(1, M + 1)}
imos = [0 for i in range(M + 2)]
for i in range(N):
    l, r = map(int, input().split())
    q[l].append(r)
    imos[l] += 1
    imos[r + 1] -= 1
for i in range(1, M + 1):
    imos[i] += imos[i - 1]
res = {i: imos[i * (M // i)] for i in range(1, M + 1)}

query = {i: [] for i in range(1, M + 1)}
for i in range(1, M + 1):
    for j in range(1, M // i):
        query[i * j].append(i * j + i)

bit = BIT(M)
for i in range(1, M + 1):
    for r in q[i]:
        bit.update(r, 1)
    for r in query[i]:
        res[r - i] += bit.query(r - 1) - bit.query(i - 1)

for i in range(1, M + 1):
    print(res[i])
