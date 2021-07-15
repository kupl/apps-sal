t=int(input())
for i in range(t):
 n,k=list(map(int,input().split()))
 arr=list(map(int,input().split()))
 arr1=list(set(arr))

 l=[]
 res=0
 sums=0
 for i in range(k):
  l.append(arr[i])
  sums+= arr[i]
 
 
 if(len(list(set(l)))==len(arr1)):
  res=max(res,sums)
 
 
 for i in range(k,n):
  sums+= (arr[i]-arr[i-k])
  l.remove(arr[i-k])
  l.append(arr[i])
  if(len(list(set(l)))==len(arr1)):
   res=max(res,sums)
 print(res)

