N,*A=map(int,open(0).read().split())
A,r,R=[[a]for a in A],0,range
for n in R(N):
 B=1<<n
 for i in R(1<<N):
  if i&B:A[i]=sorted(A[i^B]+A[i])[-2:]
for a,b in A[1:]:r=max(r,a+b);print(r)
