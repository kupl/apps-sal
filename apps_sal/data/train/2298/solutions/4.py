import heapq
(N, T) = list(map(int, input().split()))
A = list(map(int, input().split()))
h = []
B = [0] * N
for i in range(N):
    heapq.heappush(h, A[i])
    B[i] = h[0]
j = []
C = [0] * N
for i in range(N - 1, -1, -1):
    heapq.heappush(j, -A[i])
    C[i] = -j[0]
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
