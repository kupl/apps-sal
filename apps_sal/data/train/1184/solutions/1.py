# cook your dish here
f=[]
for ad in range(int(input())):
 n=int(input())
 a=[0]*4;b=[0]*4;c=[0]*4;d=[0]*4
 for i in range(n):
  x=(input().split())
  if x[0]=="A":
   a[int(x[1])//3-1]+=1
  elif x[0]=="B":
   b[int(x[1])//3-1]+=1
  elif x[0]=="C":
   c[int(x[1])//3-1]+=1
  elif x[0]=="D":
   d[int(x[1])//3-1]+=1
 x=[]
 for i in range(4):
  for j in range(4):
   for k in range(4):
    for m in range(4):
     s=0
     l=[i,j,k,m]
     if len(set(l))==4:
      y=[a[i],b[j],c[k],d[m]]
      for t in y:
       if t==0:
        s-=100
      y.sort()
      for t in range(3,-1,-1):
       s+=(25+25*t)*y[t]
      x.append(s)
 
 m=max(x)
 f.append(m)
 print(m)
print(sum(f))

