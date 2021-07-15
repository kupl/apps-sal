x=int(input())
for i in range(x):
 friends=int(input())
 arr=list(map(int,input().split()))
 arr.sort()
 tot=0
 for ele in arr:
  if ele<=tot:
   tot+=1
 print(tot)

