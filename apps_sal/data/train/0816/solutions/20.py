n=int(input())
arr=[int(x) for x in input().split()]
m=int(input())
for _ in range(m) :
    q=int(input())
    val=arr[q-1]
    print(val)
    arr.remove(val)
