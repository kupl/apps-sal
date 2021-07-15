# cook your dish here
for _ in range(int(input())):
 n=int(input())
 s=input()
 ans=s
 for i in range(n):
  new_s=s[:i]+s[i+1:]
  for j in range(n):
   ans=min(ans,new_s[:j]+s[i]+new_s[j:])
   
 print(ans)
