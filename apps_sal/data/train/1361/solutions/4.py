n,k1 = map(int, input().split())
arr  = list(map(int, input().split()))
for i in range(k1):
    for j in range(1,n):
        arr[j]=arr[j]+arr[j-1]
for k in range(len(arr)):
    print(arr[k]%1000000007,end=" ")


