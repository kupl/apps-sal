N = int(input())
A = list(map(int, input().split()))
XOR = 0
for a in A:
    XOR ^= a
for i in range(N):
    A[i] = A[i] ^ XOR
print(*A)
