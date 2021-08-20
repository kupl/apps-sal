from collections import defaultdict


def trans(arr, n):
    temp = [0] * n
    return change(arr, temp, 0, n - 1)


def change(arr, temp, left, right):
    rep = 0
    if left < right:
        mid = (left + right) // 2
        rep += change(arr, temp, left, mid)
        rep += change(arr, temp, mid + 1, right)
        rep += merge(arr, temp, left, mid, right)
    return rep


def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    rep = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            rep += mid - i + 1
            k += 1
            j += 1
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp[loop_var]
    return rep


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    result = trans(arr, n)
    print(result)
