N = int(input())
x, y = 0, 0
A, B = [], []
for i in range(N):
    x, y = map(int, input().split())
    A.append(x)
    B.append(y)
x = sum(A)
for i in range(N):
    if A[i] > B[i]:
        x = min(x, B[i])
print(sum(A) - x)
