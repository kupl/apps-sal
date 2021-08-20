(n, k) = map(int, input().split())
arr = []
for i in range(n):
    arr += [int(input())]
arr.sort()
ans = 10 ** 10
for i in range(n - k + 1):
    ans = min(ans, arr[k + i - 1] - arr[i])
print(ans)
