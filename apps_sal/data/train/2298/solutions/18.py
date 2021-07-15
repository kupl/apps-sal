N , T = list(map(int,input().split()))
A = list(map(int,input().split()))

m = 10 ** 9
L = [m] * (N)


for i in range(0,N):
  if A[i] <= m:
    m = A[i]
  L[i] = A[i] - m

M = max(L)

print((L.count(M)))
  


