for _ in range(int(input())):
 n=int(input())
 s=list(input())
 coord=list(map(int,input().split()))
 p=0
 i=0
 h=[]
 for i in range(0,n):
  if s[i]=='1':
   h.append(i)
 if h[0]!=0:
  p=p+coord[h[0]]-coord[0]
 if h[len(h)-1]!=n-1:
  p=p+coord[n-1]-coord[h[len(h)-1]]
 for j in range(0,len(h)-1):
  if h[j]+1==h[j+1]:
   continue
  if h[j+1]-h[j]-1==1:
   p=p+min(coord[h[j]+1]-coord[h[j]],coord[h[j+1]]-coord[h[j]+1])
  else:
   y=min(coord[h[j+1]]-coord[h[j]+1],coord[h[j+1]-1]-coord[h[j]])
   for k in range(h[j]+1,h[j+1]-1):
    y=min(y,coord[k]-coord[h[j]]+coord[h[j+1]]-coord[k+1])
   p=p+y
 print(p)
