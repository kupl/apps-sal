from bisect import bisect
N = int(input())
(*A,) = map(int, input().split())
(*B,) = map(int, input().split())
M = 32
MOD = [2 << i for i in range(M + 1)]


def make(B, mode):
    S = [None] * M
    s = {}
    get = s.get
    for b in B:
        s[b] = get(b, 0) ^ 1
    S[M - 1] = sorted((b for b in s if s[b]))
    for i in range(M - 2, -1, -1):
        t = S[i + 1]
        l = len(t)
        m = MOD[i]
        mid = q = bisect(t, m - 1)
        p = 0
        if q < l:
            if p < mid:

                def gen(p, q):
                    u = t[p]
                    v = t[q]
                    while p < mid and q < l:
                        if u + m == v:
                            p += 1
                            u = t[p] if p < mid else None
                            q += 1
                            v = t[q] if q < l else None
                        elif u + m < v:
                            yield u
                            p += 1
                            u = t[p] if p < mid else None
                        else:
                            yield (v - m)
                            q += 1
                            v = t[q] if q < l else None
                    while p < mid:
                        yield t[p]
                        p += 1
                    while q < l:
                        yield (t[q] - m)
                        q += 1
                (*S[i],) = gen(p, q)
            else:
                (*S[i],) = (u - m for u in t)
        else:
            (*S[i],) = t
    if mode:
        for i in range(M):
            m = MOD[i]
            S[i] += list(map(lambda x: x + m, S[i]))
    return S


S = make(A, 0)
T = make(B, 1)
ans = 0
if 0 in S[0]:
    ans ^= 1 in T[0]
if 1 in S[0]:
    ans ^= 0 in T[0]
for i in range(1, M):
    s = S[i]
    ls = len(S)
    t = T[i]
    lt = len(t)
    m = MOD[i]
    p = MOD[i - 1]
    P = p + m
    Q = 2 * m
    if lt:
        c = 0
        f = lt
        while P <= t[f - 1]:
            f -= 1
        u = f
        v = lt
        for a in s:
            while u > 0 and P <= a + t[u - 1]:
                u -= 1
            while v > 0 and Q <= a + t[v - 1]:
                v -= 1
            c += v - u
        if c & 1:
            ans ^= 1 << i
print(ans)
