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
    a = [0] * n
    for i in range(n):
        a[p[i] - 1] = i
    m = [0] * d
    inv_count = 0
    for i in range(d):
        t = (n - 1 - i) // d + 1
        h = [0] * t
        for j in range(t):
            h[j] = a[i + j * d]
        inv_count += mergesort(h, 0, len(h) - 1)
        m[i] = h
    s = [0] * n
    for i in range(d):
        t = (n - 1 - i) // d + 1
        for j in range(t):
            s[i + j * d] = m[i][j]
    mb = True
    for i in range(n):
        if s[i] == i:
            continue
        else:
            mb = False
            break
    if mb:
        print(inv_count)
    else:
        print(-1)
