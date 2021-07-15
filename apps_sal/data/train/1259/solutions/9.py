t=int(input())
for j in range(t):
 l,r=list(map(int,input().split()))
 c=0
 for i in range(l,(r+1)):
  if ((i%10)==2) or ((i%10)==3) or ((i%10)==9):
   c+=1
 print(c) 

