# cook your dish here
t=int(input())
while t>0:
    n,m=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr.sort()
    if arr[n-1]-arr[0]<m:
        print('YES')
    else:
        print('NO')
    t-=1


