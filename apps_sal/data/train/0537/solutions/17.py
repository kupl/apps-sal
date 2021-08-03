nk = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
count = 0
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        x = arr[j] - arr[i]
        if x >= nk[1]:
            count = count + 1
print(count)
3
