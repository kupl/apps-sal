t = eval(input())
for _ in range(t):
    n = eval(input())
    num = [int(i) for i in input().split()]
    arr = []
    ans = 0
    for i in range(1, n + 1):
        if(num[i - 1] == 0):
            arr[0:0] = [i]
        else:
            x = arr.index(num[i - 1]) + 1
            y = len(arr) - x
            ans += min(x, y)
            arr[x:x] = [i]
    print(ans)
