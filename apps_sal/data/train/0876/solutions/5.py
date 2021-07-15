for _ in range(int(input())):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    m=max(arr)-min(arr)
    if(m<b):
        print("YES")
    else:
        print("NO")
