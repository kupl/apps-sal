n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
count = n * (n - 1) // 2

for i in range(n - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if arr[i] - arr[j] >= k:
            break
        else:
            count -= 1

print(count)
