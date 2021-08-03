from itertools import accumulate
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

inf = 10**10

S = [0] + sorted(list(set(A)))
dic = {s: inf for s in S}
cnt = {s: 0 for s in S}
sm = {s: 0 for s in S}
ml = [0]
for i, a in enumerate(A):
    if ml[-1] < a:
        ml.append(a)
    dic[a] = min(i, dic[a])
    cnt[a] += 1
    sm[a] += a

for ps, s in zip(S[:-1][::-1], S[::-1]):
    cnt[ps] += cnt[s]
    sm[ps] += sm[s]

ans = [0] * N
temp = {s: sm[s] - s * cnt[s] for s in S}

for ps, s in zip(ml[:-1][::-1], ml[::-1]):
    ans[dic[s]] = temp[ps] - temp[s]

[print(a) for a in ans]
