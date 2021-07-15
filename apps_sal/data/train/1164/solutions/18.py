p,s=list(map(int,input().split()))
count=[0]*101010
a=[]
b=[]
for i in range(p):
 a=list(map(int,input().split()))
 b=list(map(int,input().split()))
 a,b=list(zip(*sorted(zip(a,b))))
 for x in range(len(b)-1):
  if(b[x]>b[x+1]):
   count[i]+=1
for i in range(31):
 for j in range(p):
  if(count[j]==i):
   print(j+1)

