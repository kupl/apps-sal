def brute(ind,arr,factors):
 if ind==len(factors):
  return sum(arr)
 ans=10000000000000
 for i in range(len(arr)):
  arr[i]*=factors[ind]
  ans=min(ans,brute(ind+1,arr,factors))
  arr[i] //= factors[ind]
 return ans

def factorize(x):
 factors=[]
 for i in range(2,int(x**0.5)+1):
  if x%i==0:
   count=0
   while x%i==0:
    count+=1
    x //= i
   factors.append(i**count)
 if x!=1:
  factors.append(x)
 return factors


t=int(input())
for _ in range(t):
 k,x=map(int,input().split())
 factors=factorize(x)
 if len(factors)<=k:
  print(sum(factors)+k-len(factors))
 else:
  arr = [1]*k
  print(brute(0,arr,factors))
