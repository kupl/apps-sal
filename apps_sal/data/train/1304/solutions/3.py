(n, k) = map(int, input().split())
for i in range(k):
    arr = list(map(int, input().split()))
    res = []
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            res.append(arr[i - 1])
            res.append(arr[i])
            temp = arr[i - 1]
            break
        else:
            res.append(arr[i])
    res.sort()
    for j in range(len(res)):
        if res[j] > temp:
            arr[i - 1] = res[j]
            res.remove(res[j])
            break
    for j in range(len(res)):
        arr[i] = res[j]
        i += 1
    print(*arr)
