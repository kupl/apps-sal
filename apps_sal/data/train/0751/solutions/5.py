for _ in range(int(input())):
 n=int(input())
 s=list(input())
 l=list(map(int,input().split()))
 p=0
 i=0
 h=[]
 for i in range(0,n):
  if s[i]=='1':
   h.append(i)
 if h[0]!=0:
  p=p+l[h[0]]-l[0]
 if h[len(h)-1]!=n-1:
  p=p+l[n-1]-l[h[len(h)-1]]
 for j in range(0,len(h)-1):
  if h[j]+1==h[j+1]:
   continue
  if h[j+1]-h[j]-1==1:
   p=p+min(l[h[j]+1]-l[h[j]],l[h[j+1]]-l[h[j]+1])
  else:
   y=min(l[h[j+1]]-l[h[j]+1],l[h[j+1]-1]-l[h[j]])
   for k in range(h[j]+1,h[j+1]-1):
    y=min(y,l[k]-l[h[j]]+l[h[j+1]]-l[k+1])
   p=p+y
 print(p)
    
   
   

