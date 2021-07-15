t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    for i in range(n):
        if arr[i]%6==0:
            arr[i]=6
        else:
            arr[i]=arr[i]%6
    print(sum(arr))        

