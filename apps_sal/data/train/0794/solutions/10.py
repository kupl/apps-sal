MOD=10**9+7
T=int(input()) 
for t in range(T):
 n,m=map(int,input().split()) 
 A=list(map(int,input().split())) 
 mp=[0]*n 
 for a in A:
  mp[a]+=1 
 mx=max(A) 
 ans=1
 for i in range(1,mx):
  ans=(ans*(mp[i]**mp[i+1]))%MOD 
 print(ans)
