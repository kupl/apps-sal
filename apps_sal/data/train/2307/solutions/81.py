N,A,B=list(map(int,input().split()))
L=list(map(int,input().split()))
w=B//A
v=0
for i in range(N-1):
  d=L[i+1]-L[i]
  if d>w:
    v+=B
  else:
    v+=d*A
print(v)
