(n, k) = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
i = 0
res = 0
for j in range(n):
    while i < n:
        if arr[i] - arr[j] >= k:
            res = res + (n - i)
            break
        i += 1
print(res)
