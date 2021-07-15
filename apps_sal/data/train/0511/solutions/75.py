n = int(input())
A = list(map(int, input().split()))
X = A[0]
for a in A[1:]:
    X = X ^ a
for i in range(n):
    A[i] = str(X ^ A[i])
print(" ".join(A))
