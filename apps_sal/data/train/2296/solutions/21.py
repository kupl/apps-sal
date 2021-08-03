import sys


class BIT():
    def __init__(self, number):
        self.n = number
        self.list = [0] * (number + 1)

    def add(self, i, x):  # ith added x  1indexed
        while i <= self.n:
            self.list[i] += x
            i += i & -i

    def search(self, i):  # 1-i sum
        s = 0
        while i > 0:
            s += self.list[i]
            i -= i & -i
        return s

    def suma(self, i, j):  # i,i+1,..j sum
        return self.search(j) - self.search(i - 1)


#from collections import defaultdict
S = input()
N = len(S)
L = 26
a = ord('a')
d = [[] for i in range(L)]
for i in range(N):
    s = ord(S[i]) - a
    d[s].append(i)
flag = 0
for i in range(L):
    if len(d[i]) % 2 == 1:
        flag += 1
if flag > 1:
    print(-1)
    return
Suc = [-1] * N
pairs = []
for i in range(L):
    T = len(d[i])
    for s in range((T // 2)):
        li, ri = d[i][s], d[i][-s - 1]
        pairs.append((li, ri))
    if T % 2 == 1:
        Suc[d[i][T // 2]] = (N // 2) + 1
pairs.sort()
for i, (li, ri) in enumerate(pairs):
    Suc[li] = i + 1
    Suc[ri] = N - i
Tree = BIT(N + 3)
ans = 0
for i, m in enumerate(Suc):
    ans += i - Tree.search(m)
    Tree.add(m, 1)
# ans+=Tree.search(N+1)
print(ans)
