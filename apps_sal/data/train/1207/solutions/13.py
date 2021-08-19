t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    for i in range(1, n):
        ans = ans + arr[0] * arr[i]
    print(ans)
