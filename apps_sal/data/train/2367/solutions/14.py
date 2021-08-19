from collections import defaultdict
from math import sqrt, factorial, gcd, log2, inf, ceil
mod = 10 ** 9 + 7


def mergeSort(arr, n):
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)


def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count = _mergeSort(arr, temp_arr, left, mid)
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += mid - i + 1
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
    return inv_count


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    t = input()
    if sorted(s) != sorted(t):
        print('NO')
    else:
        hash = defaultdict(int)
        flag = 0
        for i in s:
            hash[i] += 1
            if hash[i] > 1:
                print('YES')
                flag = 1
                break
        if not flag:
            l1 = [ord(i) for i in s]
            l2 = [ord(i) for i in t]
            z1 = mergeSort(l1, n)
            z2 = mergeSort(l2, n)
            if z1 % 2 != z2 % 2:
                print('NO')
            else:
                print('YES')
