def bi(n): 
 count = 0
 while (n): 
  count += 1
  n =n&(n-1)
 return count 

t=int(input())
for q in range(t):
 n=int(input())
 b=list(map(int,input().split()))
 ans=1
 mod=(10**9)+7
 end=0
 for i in range(1,n):
  if b[i]|b[i-1]!=b[i]:
   end=1
   print(0)
   break
  else:
   k=bi(b[i]&b[i-1])
   ans=(ans*(2**k))%mod
 if end==0:
  print(ans)
