from bisect import bisect_left, insort_left
N = int(input())
S = [c for c in input()]
Q = int(input())
d = {i: [] for i in range(26)}
for i, c in enumerate(S):
    d[ord(c) - ord("a")].append(i)

# print(d)
for _ in range(Q):
    q = input().split()
    if int(q[0]) == 1:
        iq, cq = int(q[1]), q[2]
        iq -= 1
        if S[iq] == cq:
            continue
        else:
            idx = bisect_left(d[ord(S[iq]) - ord("a")], iq)
            d[ord(S[iq]) - ord("a")].pop(idx)
            S[iq] = cq
            insort_left(d[ord(cq) - ord("a")], iq)
    else:
        l, r = int(q[1]), int(q[2])
        l -= 1
        ans = 0
        for i in range(26):
            idx = bisect_left(d[i], l)
            if d[i] and l <= d[i][-1] and d[i][idx] < r:
                ans += 1
        print(ans)
