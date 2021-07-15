N = int(input())
A = list(map(int, input().split()))
b = 0
for x in A:
    b ^= x
for i in range(len(A)):
    A[i] ^= b
print(*A)
