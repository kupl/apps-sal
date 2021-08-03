N = int(input())
A = list(map(int, input().split()))
sum_xor = A[0]

for i in range(1, N):
    sum_xor ^= A[i]

for j in range(N):
    print(sum_xor ^ A[j], end=" ")
