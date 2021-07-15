# cook your dish here
t=int(input())
for i in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 c=0
 odd=0
 for k in range(n-2,-1,-1):
  if a[k+1]%2!=0:
   odd+=1
  if a[k]%2==0:
   c+=odd
 print(c)
  

