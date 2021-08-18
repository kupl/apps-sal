
t = int(input())
for d in range(t):
    n = int(input())
    n += 1
    ans = 0
    arr = list(map(int, input().split()))
    index = 1
    while(index < n):
        if(arr[index] > arr[index - 1]):
            ans = index
            break
        index += 1
    if(ans != 0):
        print(n - ans)
    else:
        print(0)
