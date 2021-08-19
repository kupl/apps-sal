arr = input().strip()
res = []
for i in range(len(arr)):
    s = int(arr[i])
    k = 0
    for j in range(i, len(arr) - 1):
        if arr[j + 1] > arr[j]:
            s = s + int(arr[j + 1])
            k += 1
        else:
            break
    res.append([i + 1, i + k + 1, s])
for i in range(len(res)):
    for j in range(i + 1, len(res)):
        if res[i][2] > res[j][2]:
            temp = res[j]
            res[j] = res[i]
            res[i] = temp
print('{}:{}-{}'.format(res[-1][2], res[-1][0], res[-1][1]))
