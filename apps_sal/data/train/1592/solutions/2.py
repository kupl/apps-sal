for i in range(int(input())):
 n=int(input())
 chef=0
 ans=[]
 for i in range(0,n):
  l=list(map(int,input().split()))
  c=l[0]
  if c%2==0:
   for i in range(1,len(l)//2+1):
    chef=chef+l[i]
   continue;
  for i in range(1,(len(l)//2)+1):
   chef=chef+l[i]
  ans.append(l[len(l)//2])
 print(chef)
   
  

