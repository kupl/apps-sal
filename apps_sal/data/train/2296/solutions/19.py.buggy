from collections import deque
from collections import Counter
S = input()
N = len(S)
ctr = Counter(S)
if len([1 for v in ctr.values() if v % 2]) > 1:
    print(-1)
    return

M = None
for k, v in ctr.items():
    if v % 2:
        M = k
    ctr[k] //= 2


def ctoi(c):
    return ord(c) - ord('a')


idxs = [deque() for _ in range(26)]
for i, c in enumerate(S):
    idxs[ctoi(c)].append(i)

A = ''
P = []
i = 0
while len(A) < N // 2:
    c = S[i]
    if ctr[c] > 0:
        ctr[c] -= 1
        A += c
        P.append(idxs[ctoi(c)].popleft())
    i += 1
if M:
    P.append(idxs[ctoi(M)].popleft())
for c in A[::-1]:
    P.append(idxs[ctoi(c)].popleft())


def inversion(inds):
    bit = [0] * (N + 1)

    def bit_add(x, w):
        while x <= N:
            bit[x] += w
            x += (x & -x)

    def bit_sum(x):
        ret = 0
        while x > 0:
            ret += bit[x]
            x -= (x & -x)
        return ret
    inv = 0
    for ind in reversed(inds):
        inv += bit_sum(ind + 1)
        bit_add(ind + 1, 1)
    return inv


print(inversion(P))
