import collections
import heapq
n = int(input())
A = [int(i) for i in input().split()]
Ans = [0] * n
M = [0]
for i in range(n):
    M.append(max(M[-1], A[i]))
D = collections.defaultdict(int)
H = []
for i in range(n):
    j = n - 1 - i
    if A[j] <= M[j]:
        heapq.heappush(H, -A[j])
    else:
        Ans[j] = (A[j] - M[j]) * (D[A[j]] + 1)
        D[M[j]] += D[A[j]] + 1
        ct = 0
        while H:
            a = heapq.heappop(H)
            a = -a
            if a <= M[j]:
                heapq.heappush(H, -a)
                break
            else:
                Ans[j] += a - M[j]
                D[M[j]] += 1

for a in Ans:
    print(a)
