def all_pcombo(arr,factors,pos):
 if pos==len(factors):
  return sum(arr)

 ans=float('inf')

 for i in range(len(arr)):
  arr[i]*=factors[pos]
  ans=min(ans,all_pcombo(arr,factors,pos+1))
  arr[i]//=factors[pos]

 return ans

def factorization(n):
 factors=[]
 for i in range(2,int(n**0.5)+1):
  if n%i==0:
   cnt=0
   while n%i==0:
    cnt+=1
    n//=i
   factors.append(i**cnt)

 if n>1:
  factors.append(n)
 return factors

def solve():
 k,x=map(int,input().split())
 factors=factorization(x)
 len_=len(factors)

 ans=0
 if len_<=k:
  ans=sum(factors) + k-len_
 else:
  arr=[1]*k
  ans=all_pcombo(arr,factors,0)

 print(ans)


t=int(input())
while t>0:
 solve()
 t-=1
