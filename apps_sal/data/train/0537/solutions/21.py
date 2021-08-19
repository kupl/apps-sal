(n, k) = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr.reverse()
count = n * (n - 1) // 2
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] - arr[j] >= k:
            break
        else:
            count -= 1
print(count)
