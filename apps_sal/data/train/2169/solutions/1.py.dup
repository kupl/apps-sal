from collections import Counter as C
N, P, K = list(map(int, input().split()))
A = [int(a) for a in input().split()]
X = C([(a**4 - K * a) % P for a in A])
ans = 0
for x in X:
    ans += X[x] * (X[x] - 1) // 2
print(ans)
