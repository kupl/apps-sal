# cook your dish here
def mergeSort(arr, n):
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)


def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0

    if left < right:
        mid = (left + right) // 2

        inv_count += _mergeSort(arr, temp_arr, left, mid)

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


t = int(input())
for _ in range(0, t):
    n, D = list([int(x) for x in input().split()])
    p = list([int(x) for x in input().split()])
    q = [0] * len(p)
    for i in range(n):
        q[p[i] - 1] = i
    sublists = []

    for i in range(0, D):
        sublist = []
        for j in range(i, len(p), D):
            sublist.append(q[j])
        sublists.append(sublist)

    flag = 0

    for i in range(0, D):
        temp_sublist = sorted(sublists[i])
        for j in range(0, len(sublists[i])):
            if i + j * D != temp_sublist[j]:
                print(-1)
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        total = sum([mergeSort(sublist, len(sublist)) for sublist in sublists])
        print(total)
