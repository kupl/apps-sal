T=int(input())
for _ in range(T):
 N=int(input())
 r=int(N**.5)
 d=N-r*r
 if d==0:
  print('X'*r+'D'*r)
 else:
  print('X'*(d%r)+'D'*(d%r>0)+'X'*(r-d%r)+'D'*(r+d//r))

