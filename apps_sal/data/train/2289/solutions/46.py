from itertools import accumulate

S = list(map(ord, input().strip()))
N = len(S)

atype = set()
seg = [0] * N
seg[-1] = 1
for i in range(N - 1, -1, -1):
    atype.add(S[i])
    if len(atype) == 26:
        atype = set()
        seg[i] = 1

inf = 1 << 32
idx = [[inf] * N for _ in range(26)]
for i in range(N - 1, -1, -1):
    s = S[i] - 97
    idx[s][i] = i

for s in range(26):
    for i in range(N - 2, -1, -1):
        idx[s][i] = min(idx[s][i], idx[s][i + 1])


seg = list(accumulate(seg[::-1]))[::-1]
seg.append(1)
L = seg[0]
ans = []
cnt = -1
for i in range(L):
    for c in range(26):
        k = idx[c][cnt + 1]
        if k == inf:
            ans.append(97 + c)
            break
        if seg[k + 1] + i + 1 <= L:
            ans.append(97 + c)
            cnt = k
            break


print(''.join(map(chr, ans)))
