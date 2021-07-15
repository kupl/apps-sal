# cook your dish here
t=int(input())
for _ in range(t):
 n=int(input())
 d={}
 for j in range(n):
  x,p,m=map(str,input().split())
  if((x,p) not in d):
   d[(x,p)]=int(m)
 lst=d.values()
 s=sum(lst)
 avg=s/n
 count=0
 
 d=sorted(d.items())
 for i in range(n):
  if(d[i][1]<avg):
   count=1
   print(d[i][0][0],d[i][0][1],d[i][1])
 if(count==0):
  print('\n')
