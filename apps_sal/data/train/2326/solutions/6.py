from heapq import heappush, heappop
N = int(input())
A = [int(a) for a in input().split()]
S = {}
m = (1 << 18) - 1
for i, a in enumerate(A):
    if a not in S:
        S[a] = (i << 18) ^ 1
    else:
        aacc = S[a]
        aa, cc = aacc >> 18, aacc & m
        S[a] = (min(aa, i) << 18) ^ (cc + 1)

H = [0]
def hpush(x): return heappush(H, -x)
def hpop(): return -heappop(H)


for a in S:
    micc = S[a]
    mi, cc = micc >> 18, micc & m
    aicc = (a << 36) ^ (mi << 18) ^ cc
    hpush(aicc)

m36 = (1 << 36) - 1
m18 = (1 << 18) - 1
ANS = [0] * N
while len(H) > 1:
    aicc = hpop()
    a = aicc >> 36
    i = (aicc >> 18) & m18
    cc = aicc & m18
    aicc = hpop()
    a2 = aicc >> 36
    i2 = (aicc >> 18) & m18
    cc2 = aicc & m18
    ANS[i] += (a - a2) * cc

    if a2 == 0:
        continue
    hpush((a2 << 36) ^ (min(i, i2) << 18) ^ (cc + cc2))

print("\n".join(map(str, ANS)))
