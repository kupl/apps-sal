import bisect
M = 1000000007
G = [0, 1, 2, 2]
currPos = 4
for i in range(3, 2000000):
    if currPos > 2000000:
        break
    j = 0
    while j < G[i] and currPos < 2000000:
        G.append(i)
        currPos += 1
        j += 1
prefixSum1 = [0]
prefixSum2 = [0]
for i in range(1, 2000000):
    prefixSum1.append(prefixSum1[i - 1] + G[i])
for i in range(1, 2000000):
    prefixSum2.append((prefixSum2[i - 1] + i * i % M * G[i] % M) % M)


def solve(n):
    nthterm = bisect.bisect_left(prefixSum1, n, lo=0, hi=len(prefixSum1)) - 0
    ans = 0
    if nthterm > 0:
        ans = prefixSum2[nthterm - 1]
    ans = (ans + nthterm * nthterm % M * (n - prefixSum1[nthterm - 1]) % M) % M
    return ans


for tc in range(int(input())):
    (l, r) = map(int, input().split())
    print((solve(r) - solve(l - 1) + M) % M)
