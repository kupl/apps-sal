# cook your dish here
for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 types=[0]*(1001)
 flag=0
 for i in range(n):
  if i!=0:
   if a[i-1]==a[i] and flag==0:
    flag=1
    continue
  types[a[i]]+=1
  flag=0
  #print(i,a[i],types)
 print(types.index(max(types)))
