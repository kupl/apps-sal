t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for j in range(n):
        if arr[j] % 2 == 0:
            ans += arr[j]
    print(ans)
