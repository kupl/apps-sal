# cook your dish here
import math
def factorize(n):
 factors=[]
 for i in range(2,int(n**0.5)+1):
  if(n%i==0):
   cntr=0
   while(n%i==0):
    cntr+=1
    n//=i
   factors.append(i**cntr)
 if n!=1:
  factors.append(n)
 return factors

def brtueforce(pos,arr,factors):
 if pos==len(factors):
  return sum(arr)
 ans=float('inf')
 for i in range(len(arr)):
  arr[i]*=factors[pos]
  ans=min(ans,brtueforce(pos+1,arr,factors))
  arr[i]//=factors[pos]

 return ans


def solve():
 #n=int(input())
 
 k,x=map(int,input().split())
 #s=input()
 #l=list(map(int,input().split()))
 #l1=list(map(int,input().split()))
 #flag=0
 
 factors=factorize(x)

 lenn=len(factors)

 if lenn<=k:

  ans=sum(factors) + k-lenn
 else:
  arr=[1]*k
  ans=brtueforce(0,arr,factors)

 print(ans)

 





t=int(input())
for i in range(t):
 solve()
