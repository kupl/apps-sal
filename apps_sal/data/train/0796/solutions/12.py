
t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [1 for _ in range(0, n)]
    for i in range(n - 2, -1, -1):
        if arr[i] * arr[i + 1] < 0:
            ans[i] = ans[i + 1] + 1
    for i in range(0, n):
        print(str(ans[i]) + " ", end="")
    print("")
