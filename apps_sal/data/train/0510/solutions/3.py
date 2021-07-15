import sys
from bisect import bisect_left, bisect_right, insort

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
S = list('-' + sr())
d = [[] for _ in range(26)]
for i in range(1, N+1):
    s = S[i]
    o = ord(s) - ord('a')
    d[o].append(i)

Q = ir()
for _ in range(Q):
    q, a, b = sr().split()
    if q == '1':
        a = int(a)
        if S[a] == b:
            continue
        prev = ord(S[a]) - ord('a')
        d[prev].pop(bisect_left(d[prev], a))
        next = ord(b) - ord('a')
        insort(d[next], a)
        S[a] = b
    else:
        left = int(a); right = int(b)
        ans = 0
        for alpha in range(26):
            index = bisect_left(d[alpha], left)
            if index < len(d[alpha]) and d[alpha][index] <= right:
                ans += 1
        print(ans)

