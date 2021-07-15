import sys
input = sys.stdin.readline
from collections import deque, defaultdict, Counter

S = input().rstrip()
L = len(S)

c = Counter(S)
if sum((x&1 for x in c.values())) >= 2:
    print(-1)
    return

alphabet_to_pos = defaultdict(deque)

for i,x in enumerate(S,1):
    alphabet_to_pos[x].append(i)

after = [None] * len(S)
n = 0
for i,x in enumerate(S,1):
    p = alphabet_to_pos[x]
    if not p:
        continue
    if len(p) == 1:
        p.pop()
        after[L//2] = i
        continue
    p.popleft()
    j = p.pop()
    after[n] = i
    after[L - n - 1] = j
    n += 1

def BIT_update(tree,x):
    while x <= L:
        tree[x] += 1
        x += x & (-x)

def BIT_sum(tree,x):
    s = 0
    while x:
        s += tree[x]
        x -= x & (-x)
    return s

answer = 0
tree = [0] * (L+1)
for i,x in enumerate(after):
    answer += i - BIT_sum(tree,x)
    BIT_update(tree,x)

print(answer)
