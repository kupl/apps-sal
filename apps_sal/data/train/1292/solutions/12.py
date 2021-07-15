# cook your dish here
x=list(map(int,input().strip().split()))
n,m,w,b=x[0],x[1],x[2],x[3]
l=[[0]*m for _ in range(n)]
for i in range(4,4+2*w,2):
  l[x[i]-1][x[i+1]-1]=1
for i in range(4+2*w,4+2*w+2*b,2):
  l[x[i]-1][x[i+1]-1]=2
ct=0
del(x)
for x in l:
  p1,p2,q=-1,-1,-1
  for i in range(m-1,-1,-1):
   if x[i]==2:
    q=i
   elif x[i]==1:
     p2=p1
     p1=i
   else:
    if q==-1 and p2==-1:
     ct+=(m-i)
    elif q==-1 and p2!=-1:
     ct+=(p2-i+1)
    elif p2==-1 and q!=-1:
     ct+=(q-i+1)
    else:
     ct+=(min(p2,q)-i+1)
   '''print(ct)
print(l)'''
print(ct)

