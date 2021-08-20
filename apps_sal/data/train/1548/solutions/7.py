for _ in range(int(input())):
    n = int(input())
    (*arr,) = map(int, input().split())
    ans = [int(1000000000.0) + 1] * n
    ans[0] = arr[0]
    for i in range(1, n):
        ans[i] = min(arr[i], ans[i], ans[i - 1] + 1)
    for i in range(n - 1)[::-1]:
        ans[i] = min(arr[i], ans[i], ans[i + 1] + 1)
    print(*ans)
