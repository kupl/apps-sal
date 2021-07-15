def factorize(n):
 factors=[]
 for i in range(2,int(n**0.5)+1):
  if n%i==0:
   cnt=0
   while n%i==0:
    cnt+=1
    n//=i
   factors.append(i**cnt)
 if n!=1:
  factors.append(n)
 return factors

def brute(pos,arr,factors):
 if pos==len(factors):
  return sum(arr)
 ans = float('inf')
 for i in range(len(arr)):
  arr[i]*=factors[pos]
  ans=min(ans,brute(pos+1,arr,factors))
  arr[i]//=factors[pos]
 return ans

t = int(input())
while t:
 k,x=map(int,input().split())
 factors=factorize(x)
 if len(factors)<=k:
  ans=sum(factors)+k-len(factors)
 else:
  arr=[1]*k
  ans=brute(0,arr,factors)
 print(ans)
 t-=1
