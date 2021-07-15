mod=10**9+7
for _ in range(int(input())):
    n,k,m=list(map(int,input().split()))
    a=list([(int(x)-1)%m+1 for x in input().split()])
    arr=[0]*k
    arr.insert(0,1)
    for i in range(n):
     end=a[i]+m*((k-a[i])//m)
     for j in range(end,a[i]-1,-m):
      arr[j]=(arr[j]+arr[j-1])%mod
    print(arr[-1])
 

