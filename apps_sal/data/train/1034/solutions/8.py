def find_div(x):
 b=[]
 e=int(x**0.5)+1
 for i in range(2,e):
  if x%i==0:
   c=0
   while x%i==0:
    c+=1
    x=x//i
   b.append(i**c)
 if x!=1:
  b.append(x)
 return b 
 
def solve(a,div,pos):
 if pos==len(div):
  return sum(a)
 ans=2**30
 for i in range(len(a)):
  a[i]*=div[pos]
  ans=min(ans,solve(a,div,pos+1))
  a[i]=a[i]//div[pos]
 return ans
 
 
t=int(input())
for _ in range(t):
 k,x=map(int,input().split())
 div=find_div(x)
 if len(div)<=k:
  ans=sum(div)+k-len(div)
 else:
  a=[1]*k
  ans=solve(a,div,0)
 print(ans) 
