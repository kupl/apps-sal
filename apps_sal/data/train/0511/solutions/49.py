N = int(input())
A = list(map(int, input().split()))
total = A[0]
for i in range(1, N):
    total ^= A[i]
for i in range(N):
    print(total ^ A[i], end=" ")
