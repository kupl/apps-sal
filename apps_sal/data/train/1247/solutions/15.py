def merge(arr, start, mid, end):
    p = start
    q = mid + 1
    k = 0
    inv = 0
    temp = [0] * len(arr)
    for i in range(start, end + 1):
        if p > mid:
            temp[k] = arr[q]
            k += 1
            q += 1
        elif q > end:
            temp[k] = arr[p]
            k += 1
            p += 1
        elif arr[p] <= arr[q]:
            temp[k] = arr[p]
            p += 1
            k += 1
        else:
            temp[k] = arr[q]
            q += 1
            k += 1
            inv += mid - p + 1
    for i in range(k):
        arr[start] = temp[i]
        start += 1
    return inv


def mergesort(arr, start, end):
    inv_count = 0
    if start < end:
        mid = (start + end) // 2
        inv_count += mergesort(arr, start, mid)
        inv_count += mergesort(arr, mid + 1, end)
        inv_count += merge(arr, start, mid, end)
    return inv_count


for _ in range(int(input())):
    (n, d) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    inv_count = 0
    m = [0] * n
    sb = True
    for i in range(d):
        k = 0
        for j in range(i, n, d):
            m[k] = p[j]
            k += 1
        b = m[0:k]
        inv_count += mergesort(b, 0, k - 1)
        k = 0
        for j in range(i, n, d):
            if not b[k] == j + 1:
                sb = False
                break
            k += 1
    if sb:
        print(inv_count)
    else:
        print(-1)
