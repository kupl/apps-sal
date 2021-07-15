from collections import Counter, defaultdict


class Bit:
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
C = Counter(S)
if len(S) % 2 == 0:
    for x in list(C.values()):
        if x % 2 == 1:
            print((-1))
            return
else:
    cnt = 0
    for x in list(C.values()):
        if x % 2 == 1:
            cnt += 1
        if cnt > 1:
            print((-1))
            return

cnt1 = 1
cnt2 = (N + 1) // 2 + 1
cnt_char = defaultdict(int)
seq = [0] * N
S1 = []
S2 = []
for i, s in enumerate(S):
    cnt_char[s] += 1
    if C[s] % 2 == 1:
        if cnt_char[s] == C[s] // 2 + 1:
            seq[i] = N // 2 + 1
            continue
    if cnt_char[s] <= C[s] // 2:
        seq[i] = cnt1
        cnt1 += 1
        S1.append(s)
    else:
        seq[i] = cnt2
        cnt2 += 1
        S2.append(s)
S2.reverse()

ans = 0
seq.reverse()
bit1 = Bit(N+1)
for i in range(N):
    ans += bit1.sum(seq[i])
    bit1.add(seq[i], 1)

char2idx = defaultdict(list)
for i, s1 in enumerate(S1):
    char2idx[s1].append(i+1)
for x in list(char2idx.keys()):
    char2idx[x].reverse()

seq_ = []
for i, s2 in enumerate(S2):
    seq_.append(char2idx[s2].pop())

bit2 = Bit(N+1)
seq_.reverse()
for i in range(len(seq_)):
    ans += bit2.sum(seq_[i])
    bit2.add(seq_[i], 1)

print(ans)

