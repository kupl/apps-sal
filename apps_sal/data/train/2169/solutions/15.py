from collections import Counter
N, mod, K = map(int, input().split())
A = list(map(int, input().split()))
C = Counter()
for a in A:
    C[(a**4 - a*K)%mod] += 1

ans = 0

for v in C.values():
    ans += v*(v-1)//2

print(ans)
