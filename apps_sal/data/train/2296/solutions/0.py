import collections


class Bit():
    def __init__(self, l):
        self.size = l
        self.bit = [0] * (self.size+1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

    def __str__(self):
        return str(self.bit)


S = str(input())
N = len(S)
index = collections.defaultdict(list)

for i, c in enumerate(S):
    index[c].append(i)

ctr = N // 2
B = [0] * N
flag = 0
P = []

for c, k in list(index.items()):
    cnt = len(k)
    if cnt % 2:
        if flag == 1:
            print((-1))
            return
        flag = 1
        B[k[cnt // 2]] = ctr + 1
    for i in range(cnt // 2):
        l, r = k[i], k[-(i+1)]
        P.append((l, r))

P.sort()

for i, (l, r) in enumerate(P):
    B[l], B[r] = i + 1, N - i

ans = 0
bit = Bit(N)
for i, b in enumerate(B):
    ans += i - bit.sum(b)
    bit.add(b, 1)

print(ans)

