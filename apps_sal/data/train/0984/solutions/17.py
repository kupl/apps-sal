t=int(input())
for i in range(t):
 n=int(input())
 ans=0
 a=list(map(int,input().split()))
 for j in range(len(a)-1):
  for k in range(j+1,len(a)):
   if j<k and a[j]%2==0 and a[k]%2!=0:
    ans+=1
 print(ans) 

