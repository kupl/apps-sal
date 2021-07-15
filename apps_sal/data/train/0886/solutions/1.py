for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    m=int(input())
    s=999999999;l=999999999;an=-1;pj=-1
    for i in range(n):
        arr[i]+=arr[i]%3
        if(arr[i] > m and arr[i]-m<l):
            an=arr[i]
            l=arr[i]-m
        if(arr[i]<m and m-arr[i]<s):
            pj=arr[i]
            s=m-arr[i]
    print(pj,an)
