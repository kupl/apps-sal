# cook your dish here
tc=int(input())
for j in range(tc):
 ip=list(map(int,input().rstrip().split()))
 x=ip[0]
 y=ip[1]
 n=ip[2]
 cnt=0
 for i in range(n+1):
  if((x^i)<(y^i)):
   cnt+=1 
 print(cnt)
