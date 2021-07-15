from math import pi
from cmath import exp
def fft(a, lgN, rot=1): # rot=-1 for ifft
  N = 1<<lgN
  assert len(a)==N
  rev = [0]*N
  for i in range(N):
    rev[i] = (rev[i>>1]>>1)+(i&1)*(N>>1)
  A = [a[rev[i]] for i in range(N)]
  h = 1
  while h<N:
    w_m = exp((0+1j) * rot * (pi / h))
    for k in range(0, N, h<<1):
      w = 1
      for j in range(h):
        t = w * A[k+j+h]
        A[k+j+h] = A[k+j]-t
        A[k+j] = A[k+j]+t
        w *= w_m
    h = h<<1
  return A if rot==1 else [x/N for x in A]


import sys
ints = (int(x) for x in sys.stdin.read().split())

n, x = (next(ints) for i in range(2))
r = [next(ints) for i in range(n)]
ac = [0]*(n+1)
for i in range(n): ac[i+1] = (r[i]<x) + ac[i]

# Multiset addition
min_A, min_B = 0, -ac[-1]
max_A, max_B = ac[-1], 0
N, lgN, m = 1, 0, 2*max(max_A-min_A+1, max_B-min_B+1)
while N<m: N,lgN = N<<1,lgN+1
a, b = [0]*N, [0]*N
for x in ac:
  a[x-min_A] += 1
  b[-x-min_B] += 1
c = zip(fft(a, lgN), fft(b, lgN))
c = fft([x*y for x,y in c], lgN, rot=-1)
c = [round(x.real) for x in c][-min_A-min_B:][:n+1]
c[0] = sum((x*(x-1))//2 for x in a)
print(*c, *(0 for i in range(n+1-len(c))), flush=True)
