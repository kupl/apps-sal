import sys
from bisect import bisect_left, bisect_right, insort


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N = ir()
S = list('-' + sr())
d = [[] for _ in range(26)]
for i in range(1, N + 1):
    s = S[i]
    o = ord(s) - ord('a')
    insort(d[o], i)

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
        a = int(a)
        b = int(b)
        ans = 0
        for alpha in range(26):
            if bisect_right(d[alpha], b) - bisect_left(d[alpha], a) >= 1:
                ans += 1
        print(ans)
