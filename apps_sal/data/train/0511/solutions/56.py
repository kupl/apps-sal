N = int(input())
A = list(map(int, input().split()))
X = A[0]
for i in range(1, N):
    X ^= A[i]

for i in range(N):
    print(X ^ A[i], end=' ')
