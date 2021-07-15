n=int(input())
arr=list(map(int,input().split()))
m=int(input())
for i in range(m):
    x,y=map(int,input().split())
    branch=x-1
    left=y-1
    right=arr[branch]-y
    if branch-1<0:
        if branch+1<n:
            arr[branch+1]+=right
    elif branch+1>=n:
        if branch-1>=0:
            arr[branch-1]+=left
    else:
        arr[branch-1]+=left
        arr[branch+1]+=right
    arr[branch]=0
for i in range(n):
    print(arr[i])
