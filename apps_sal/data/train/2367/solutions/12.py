q = int(input())


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
            inv_count += (mid - i + 1)
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


for i in range(q):
    l = int(input())
    s1 = input()
    s2 = input()

    if sorted(s1) != sorted(s2):
        print("NO")
        continue

    if len(s1) != len(set(s1)):
        print("YES")
        continue
    if len(s2) != len(set(s2)):
        print("YES")
        continue

    arr = [s2.index(c) for c in s1]

    if mergeSort(arr, len(arr)) % 2 == 0:
        print("YES")
    else:
        print("NO")
