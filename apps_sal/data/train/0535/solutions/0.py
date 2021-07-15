def C(n):
 return n*(n-1)//2


def sol():
 equal, mini = False, min(N,M)
 total_ways = 2*C(N * M)
 if N==M:
  equal = True
 ways = 0
 if not equal:
  ways = (N*C(M)+M*C(N))
  diag = 0
  for i in range(2, mini+1):
   diag += 2*C(i)
  for i in range(mini+1,max(N,M)):
   diag += C(mini)
  diag *= 2
  ways += diag
  ways *= 2
 else:
  ways = (N*C(M)+M*C(N))
  diag = 0
  for i in range(2, mini):
   diag += 2*C(i)
  diag += C(mini)
  diag *= 2
  ways += diag
  ways *=2
 safe = total_ways - ways
 l, r, t, d = Y-1, M-Y, X-1, N-X
 safe_add, to_remove = 0, 0

 for i in range(1,N+1):
  for j in range(1, M+1):
   if i==X or j==Y or abs(i-X)==abs(j-Y):
    continue
   else:
    to_remove += 1

 if l>0 and r>0 and t>0 and d>0:
  dtl, dtr, dbl, dbr = min(l,t), min(r,t), min(l,d), min(r,d)
  safe_add += dtl*dbr*2 + dtr*dbl*2
  safe_add += t*d*2
  safe_add += l*r*2
 elif l>0 and r>0:
  safe_add += l*r*2
 elif t>0 and d>0:
  safe_add += t*d*2

 safe += safe_add - to_remove*2

 return safe


T = int(input())
for _ in range(T):
 N, M, X, Y = [int(x) for x in input().split()]
 print(sol())
