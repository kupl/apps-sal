n=int(input())
arr=list(map(int,input().split()))
k=int(input())
for _ in range(k):
    no=int(input())
    print(str(arr[no-1]))
    arr.remove(arr[no-1])

