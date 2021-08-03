from collections import defaultdict


class BIT():
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


s = input()
n = len(s)
idx = defaultdict(list)
for i, c in enumerate(s):
    idx[c].append(i)
ctr = n // 2
B = [0] * n
flag = False
P = []
for c, I in idx.items():
    cnt = len(I)
    if cnt % 2:
        if flag:
            print(-1)
            return
        flag = True
        B[I[cnt // 2]] = ctr + 1
    for i in range(cnt // 2):
        l, r = I[i], I[-i - 1]
        P.append((l, r))
P.sort()
for i, (l, r) in enumerate(P):
    B[l], B[r] = i + 1, n - i
ans = 0
bit = BIT(n)
for i, b in enumerate(B):
    ans += i - bit.sum(b)
    bit.add(b, 1)
print(ans)
