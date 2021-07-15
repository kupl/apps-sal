t=int(input())
for i in range(t):
 [a,b]=list(map(int,input().split()))
 gr=0
 for j in range(1,max(a,b)+1):
  if a%j==0 and b%j==0:
   gr=j
 print(gr) 
