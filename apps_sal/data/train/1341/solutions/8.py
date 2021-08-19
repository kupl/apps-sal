def bin(arr, l, r, val, n):
    ans = n
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= val:
            l = mid + 1
        else:
            ans = mid
            r = mid - 1
    return ans


t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    pre = []
    suff = [0] * n
    pre.append(1)
    for i in range(1, n):
        if arr[i] > arr[i - 1] and pre[i - 1] == 1:
            pre.append(1)
        else:
            pre.append(0)
    flag = 0
    temp = 0
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            suff[i] = 1
        elif arr[i] < arr[i + 1] and suff[i + 1] == 1:
            suff[i] = 1
        elif flag == 0:
            temp = i + 1
            suff[i] = 0
            flag = 1
        else:
            suff[i] = 0
    count = 0
    y = n
    for i in range(n):
        y = n
        if pre[i] == 1:
            count += 1
            if temp > i + 1:
                y = bin(arr, temp, n - 1, arr[i], n)
            elif i + 2 < n:
                y = bin(arr, i + 2, n - 1, arr[i], n)
            count += n - y
    count += n - temp
    if pre[temp] == 1:
        count -= 2
    print(count)
    t -= 1
