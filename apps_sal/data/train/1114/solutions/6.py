# cook your dish here
t=int(input())
while t>0:
 n=int(input())
 a=list(map(int,input().split()))
 max=0
 c=0
 for i in range(n):
  for j in range(i+1,n):
   if a[i]+a[j]>max:
    max=a[i]+a[j]
 for i in range(n):
  for j in range(i+1,n):
   if a[i]+a[j]==max:
    c+=1
 x=n*(n-1)/2
 print(c/x)
 t-=1
