# cook your dish here
for _ in range(int(input())):
 n=int(input())
 lst=list(map(int,input().split()))
 distance=0
 fuel=lst[0]
 for i in range(1,n):
  if fuel==0:
   break
  else:
   fuel+=lst[i]-1
   distance+=1
 print(distance+fuel)
