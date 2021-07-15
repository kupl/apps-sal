# cook your dish here
def fact(n):
 res=1
 for i in range(1,n+1):
  res*=i
 return res
t=int(input())
for _ in range(t):
 n,k=list(map(int,input().split()))
 arr=list(map(int,input().split()))
 arr.sort()
 tot=0
 for i in range(k):
  tot+=arr[i]
 count=0
 for i in range(n):
  if arr[i]==arr[k-1]:
   count+=1

 orig_count=0
 for i in range(k):
  if arr[i]==arr[k-1]:
   orig_count+=1
 print(fact(count)//(fact(orig_count)*fact(count-orig_count)))
  
  
 

