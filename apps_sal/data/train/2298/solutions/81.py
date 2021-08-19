(N, T) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [0] * N
C = [0] * N
h = A[0]
B[0] = h
for i in range(1, N):
    h = min(A[i], h)
    B[i] = h
h = A[-1]
C[-1] = h
for i in range(N - 2, -1, -1):
    h = max(A[i], h)
    C[i] = h
B = B[:-1]
C = C[1:]
D = list([C[x] - B[x] for x in range(N - 1)])
t = max(D)
s = 0
D.append(0)
for i in range(N - 1):
    if D[i] == t and D[i] > D[i + 1]:
        s += 1
print(s)
