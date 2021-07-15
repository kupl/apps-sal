mod=10**9+7
fib=[1,1]
for i in range(10**5+4):
 fib.append((fib[-1]+fib[-2])%mod)
s=input()
if 'c' in s or 'k' in s:
 print(0)
 return
n=len(s)
l=[]
i=0
while i<n:
 if s[i]=='f':
  c=0
  while i<n and s[i]=='f':
   c+=1
   i+=1
  l.append(fib[c])
 elif s[i]=='g':
  c=0
  while i<n and s[i]=='g':
   c+=1
   i+=1
  l.append(fib[c])
 else:
  i+=1
if len(l)==0:
 print(1)
 return
ans=l[0]
for i in range(1,len(l)):
 ans=(ans*l[i])%mod
print(ans)
