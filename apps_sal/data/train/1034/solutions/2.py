# cook your dish here

def factorize(n):
 fact=[]
 for i in range(2,int(n**0.5)+1):
  if n%i==0:
   c=0
   while n%i==0:
    c+=1
    n//=i
   fact.append(i**c)
 if n!=1:
  fact.append(n)
  
 return fact

def brute(pos,ar,fact):
 if pos==len(fact):
  return sum(ar)
 ans=float('inf')
 
 for i in range(len(ar)):
  ar[i]*=fact[pos]
  ans=min(ans,brute(pos+1,ar,fact))
  ar[i]//=fact[pos]
  
 return ans
 
t=int(input())

while(t>0):
 
 k,x=map(int,input().split())
 fact=factorize(x)
 lenn=len(fact)
 
 if lenn <=k:
  
  ans= sum(fact)+k-lenn
 else:
  ar=[1]*k
  ans=brute(0,ar,fact)
 print(ans)
 t-=1
