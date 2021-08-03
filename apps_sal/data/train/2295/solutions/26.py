N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    a, b = list(map(int, input().split()))
    A[i] = a
    B[i] = b

num = 10**9 + 1
for i in range(N):
    if A[i] > B[i]:
        num = min(num, B[i])

if num == 10**9 + 1:
    print((0))
else:
    print((sum(A) - num))
