t = int(input())
while t:
    t -= 1
    (n,) = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append([int(x) for x in input().split()])
    for i in range(n - 1):
        for j in range(n - 1):
            arr[i + 1][j + 1] += arr[i][j]
    ans = -float('inf')
    for i in range(n):
        for j in range(n):
            ans = max(ans, arr[i][j])
    print(ans)
