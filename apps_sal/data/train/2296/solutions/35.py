from collections import defaultdict, deque
from heapq import heappop, heappush
from string import ascii_lowercase as abc

class BIT:
    def __init__(self, N):
        # Nは入れたい要素の個数
        self.size = 2 ** (int.bit_length(N+1))
        self.tree = [0]*(self.size + 1)
 
    def sum(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= (i & -(i))
        return res
 
    def add(self, i, x):
        if i == 0:
            return
        while i <= self.size:
            self.tree[i] += x
            i += (i & -(i))


D = [deque() for _ in range(26)]
S = input()
N = len(S)

for i in range(len(S)):
    D[ord(S[i])-97].append(i)

M = [len(D[i])%2 for i in range(26)]
if sum(M) >= 2:
    print(-1)
    return

odd = sum(M)

Q = []
for c in range(26):
    if len(D[c]) >= 2:
        l = D[c].popleft()
        r = D[c].pop()
        a = l * 1
        b = N - 1 - r
        if b < a:
            a, b = b, a
        heappush(Q, (a, b, l, r, c))

T = [0]*(N//2)
for i in range(N//2):
    _, _, l, r, c = heappop(Q)
    T[i] = c

    if len(D[c]) >= 2:
        l = D[c].popleft()
        r = D[c].pop()
        a = l * 1
        b = N - 1 - r
        if b < a:
            a, b = b, a
        heappush(Q, (a, b, l, r, c))

L = [[] for i in range(26)]

for i in range(N//2):
    L[T[i]].append(N-1-i)

if odd:
    L[M.index(1)].append(N//2)

for i in range(N//2-1, -1, -1):
    L[T[i]].append(i)

bit = BIT(N)
ans = 0
for i in range(N):
    j = L[ord(S[i]) - 97].pop()
    ans += i - bit.sum(j+1)
    bit.add(j+1, 1)
print(ans)
