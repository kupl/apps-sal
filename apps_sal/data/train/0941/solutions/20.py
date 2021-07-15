n=int(input())
l=[]
for i in range(0,n):
 a,b=map(int, input().split())
 count=0
 for j in range(0,a):
  for k in range(0,b):
   if(j+k)%2==0:
    count+=1
 l.append(count)
for i in l:
 print(i)
