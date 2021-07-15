T=int(input())
for _ in range(T):
 N=int(input())
 r=int(N**.5)
 d=N-r*r
 print('X'*(d%r)+'D'*(d%r>0)+'X'*(r-d%r)+'D'*(r+d//r))

