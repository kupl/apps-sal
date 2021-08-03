N = int(input())
A = list(map(int, input().split()))
count = 0
for i in A:
    count ^= i
for i in range(len(A)):
    A[i] ^= count


print(*A)
