import bisect
from collections import defaultdict

N = int(input())
S = [*input()]
Q = int(input())
d = defaultdict(list)

for i, c in enumerate(S):
    d[c] += [i]


for _ in range(Q):
    q, y, z = input().split()

    if q == '1':
        i = int(y) - 1

        if S[i] == z:
            continue

        b = bisect.bisect(d[S[i]], i)
        d[S[i]].pop(b - 1)

        S[i] = z
        bisect.insort(d[z], i)

    else:
        left = int(y) - 1
        right = int(z) - 1

        count = 0
        for v in d.values():
            count += 1 if bisect.bisect(v, right) - bisect.bisect_left(v, left) > 0 else 0

        print(count)
