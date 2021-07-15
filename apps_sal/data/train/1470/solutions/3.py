e=10**9+7
t=int(input())
for _ in range(t):
 s=input()
 ans=0
 n=len(s)
 i=1
 m=1
 while i<n and s[i]==s[i-1]:
  m+=1
  i+=1
 ans+=(m*(m-1))//2
 while i<n:
  x=s[i-1]
  i+=1
  m=1
  while i<n and s[i]==s[i-1]:
   m+=1
   i+=1
  ans+=(m*(m-1))//2
  if i!=n and s[i]==x:
   ans+=1
 print(ans)

