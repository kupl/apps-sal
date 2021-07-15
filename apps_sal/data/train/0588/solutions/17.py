T=int(input())
def gcd(a,b):
 if(b==0):
  return a
 else:
  return gcd(b,a%b)
for i in range(T):
 N=int(input())
 arrst=input()
 arr=list(map(int,arrst.split()))
 count=0
 arr.sort()
 lis=[arr[0]-arr[len(arr)-1]+360]
 
 for j in range(len(arr)-1):
  lis+=[arr[j+1]-arr[j]]
 ans=lis[0] 
 for j in range(len(arr)):
  ans=gcd(ans,lis[j])
 for j in range(len(arr)):
  count+=(lis[j]//ans)-1
 print(int(count)) 
 


