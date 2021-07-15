import numpy
for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 ans=float('-inf')
 iidx=0
 fidx=0
 for i in range(len(l) + 1):
  for j in range(i + 1, len(l) + 1):
   sub = l[i:j]

   if len(sub)==0:
    continue
   p=numpy.prod(sub)
   if p>=ans:
    ans=p
    if i>=iidx:
     iidx=i
     if j>=fidx:
      fidx=j
 print(ans,iidx,fidx-1)


