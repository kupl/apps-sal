t=int(input())
for i in range(t):
 n,k=map(int,input().split())
 a=list(map(int,input().split()))
 lt=list()
 nos=list()
 p=-1
 for j in range(n):
  if a[j]>k:
   nos.append(a[j]) 
   lt.append(j+1)
 lt=[0]+lt+[n+1] 
 l,j=0,0
 tm=len(lt)
 nos=[0]+nos+[nos[tm-3]]
 while(j<tm-2):
  xt=j+2
  while xt+1<tm and nos[xt]==nos[j+1]:
    xt+=1
  ct=lt[xt]-lt[j]-1
  if ct>l:
   l=ct
  j=xt-1 
 print(l)
