import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))
K = 100 + max(A)
L = [0] * K
for a in A:
    L[a] += 1

for i in range(K):
    if L[i] > 1:
        L[i + 1] += L[i] // 2
        L[i] = L[i] % 2
print(sum(L))
