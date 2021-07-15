t=int(input())
 
while t>0:
 n,d = list(map(int, input().split()))
 arr=list(map(int, input().split()))
 count=0
 sum1=sum(arr)
 
 if sum1%n != 0:
  print("-1")

 else:
  ans=0
  average = sum1/n
  for i in range(0,n):
   if arr[i] != average and i+d>=n:
    ans=-1
    break
   else:
    y=arr[i]-average
    ans+=abs(y)
    if i+d < n:
     arr[i+d]+=y

     
  print(ans)
   
 t=t-1 

