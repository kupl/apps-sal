# cook your dish here
for i in range(int(input())):
 a=int(input())
 l=list(map(int,input().split()))
 s,r=0,1
 for i in range(a-1):
  if l[i]<=l[i+1]:
   s+=r+1
   r+=1
  else:
   r=1
   s+=1
 print(s+1)
