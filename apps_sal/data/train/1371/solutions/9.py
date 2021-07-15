# cook your dish here
for i in range(int(input())):
 N,T=map(int,input().split())
 L=list(map(int,input().split()))
 count=0
 for i in L:
  if (i+T)%7==0:
   count+=1
 print(count)
