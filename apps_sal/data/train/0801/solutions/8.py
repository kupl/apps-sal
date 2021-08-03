for i in range(int(input())):
    n = int(input())
    a = []
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = 10**6
    arr = [0] * (10**6 + 1)
    for i in range(n):
        arr[a[i]] += 1
        arr[b[i]] += 1
        m = min(m, a[i], b[i])
    f = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            f = -1
            break
        else:
            arr[i] = arr[i] // 2
    a1, b1 = [], []
    bn = arr.copy()
    an = arr.copy()
    for i in range(n):
        if an[a[i]]:
            an[a[i]] -= 1
        else:
            a1.append(a[i])
    for i in range(n):
        if bn[b[i]]:
            bn[b[i]] -= 1
        else:
            b1.append(b[i])
    a1.sort()
    b1.sort(reverse=True)
    if len(a1) != len(b1):
        f = -1
    if f == -1:
        print(-1)
    else:
        count = 0
        for i in range(len(a1)):
            count += min(2 * m, a1[i], b1[i])
        print(count)
