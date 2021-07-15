t=int(input())
for _ in range(t):
 s=list(input())
 n=len(s)
 ans=0
 c=0
 for i in range(0,n-1):
  if s[i]==s[i+1]:
   ans+=(n*(n+1))//2 -n 
  else:
   ans+=n
 print(ans) 
