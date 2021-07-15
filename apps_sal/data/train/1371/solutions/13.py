# cook your dish here
t=int(input())
while t!=0:
 n,k=map(int,input().split())
 arr=[int(k) for k in input().split()]
 ct=0
 for i in arr:
  if (i+k)%7==0:
   ct+=1
 print(ct)
 t-=1
