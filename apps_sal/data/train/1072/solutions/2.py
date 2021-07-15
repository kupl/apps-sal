T=int(input())
for _ in range(T):
 N=int(input())
 r=int(N**.5)
 d=N-r*r
 m=d%r
 print('X'*m+'D'*(m>0)+'X'*(r-m)+'D'*(r+d//r))

