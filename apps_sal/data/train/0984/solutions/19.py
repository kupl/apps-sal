# cook your dish here
t=int(input())
for i in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 c=0
 for k in range(0,n):
  if (a[k]%2)==0:
   for j in range(k+1,n):
    if (a[j]%2)!=0:
     c+=1
 print(c)

