from collections import Counter
class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

S = input()
N = len(S)

cnt = 0
SC = Counter(S)
for v in SC.values():
    if v % 2:
        cnt += 1
if cnt > 1:
    print(-1)
    return

geta = 10**9+7
T = [None]*N
table = Counter()
idx = dict()
ctr = 0
for i, s in enumerate(S):
    table[s] += 1
    if table[s] <= SC[s]//2: 
        T[i] = ctr
        idx[ord(s)*geta + table[s]] = ctr
        ctr += 1
        continue
    if table[s] > (1+SC[s])//2:
        T[i] = N - 1 - idx[ord(s)*geta+(SC[s] + 1 - table[s])]
        continue
    if SC[s] % 2 and table[s] == (SC[s]+1)//2:
        T[i] = (N-1)//2
        continue
Tr = [None]*N
for i, v in enumerate(T):
    Tr[v] = i
B = BIT(N)
ans = 0
for tr in Tr[::-1]:
    ans += B.sum(tr + 1)
    B.add(tr + 1, 1)
print(ans)
