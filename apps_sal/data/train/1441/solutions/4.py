for _ in range(int(input())):
 n,k=list(map(int,input().split()))
 a=list(map(int,input().split()))
 s=list(map(int,input().split()))
 m=-1;p=-1
 for i in range(n):
  if a[i]>m:
   m=a[i]
   p=i+1
 dp=[False]*(p+1)
 s.sort()
 #print(s)
 for i in range(1,p+1):
  flag=0;
  for j in range(k):
   if s[j]<=i:
    if dp[i-s[j]]==False:
     dp[i]=True
     break
   else:
    if s[j]-i<=n-p:
     dp[i]=True
     break
 if dp[-1]==False:
  print('Garry')
 else:
  print('Chef')

