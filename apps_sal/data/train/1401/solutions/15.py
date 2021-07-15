n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr=sorted(arr)
count=0
i=0
while(i<len(arr) and arr[i]<=k):
 if(arr[i]<=k):
  count+=1
  k=k-arr[i]
 i+=1
print(count)
