from collections import Counter
import sys
s = input()
N = len(s)
sc = Counter(s)
odds = [1 for x in sc if sc[x] % 2 == 1]
if len(odds) > 1:
    print((-1))
    return

class BIT:
    def __init__(self, size):
        self.bit = [0] * (size+1)
    def add(self, index, elem):
        index += 1
        while index < len(self.bit):
            self.bit[index] += elem
            index += index & -index
    def get(self, index):
        index += 1
        ret = 0
        while 0 < index:
            ret += self.bit[index]
            index -= index & -index
        return ret

indices = [-1] * N
tb = {c: [None] * (sc[c]//2) for c in sc}
lens = {c: 0 for c in sc}
p = 0
for i in range(N):
    c = s[i]
    l = lens[c]
    if 2 * (l+1) <= sc[c]:
        indices[p] = i
        tb[c][l] = p
        lens[c] += 1
        p += 1
    elif 2 * (l+1) == sc[c] + 1:
        indices[N//2] = i
        lens[c] += 1
    else:
        indices[N-1-tb[c][sc[c]-l-1]] = i
        lens[c] += 1

ans = 0
bit = BIT(N)
for i in indices:
    bit.add(i, 1)
    ans += bit.get(N-1) - bit.get(i)
print(ans)

