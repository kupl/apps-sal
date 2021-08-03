t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input(). strip(). split()))
    a = [0] * n
    b = [0] * n
    if arr[0] >= 1:
        a[0] += 1
        b[0] += 1
    if arr[-1] >= 1:
        a[-1] += 1
        b[-1] += 1
    for i in range(1, n):
        if arr[i] >= a[i - 1] + 1:
            a[i] = a[i - 1] + 1
        else:
            a[i] = arr[i]
    for j in range(n - 2, -1, -1):
        if arr[j] >= b[j + 1] + 1:
            b[j] = b[j + 1] + 1
        else:
            b[j] = arr[j]
    max = 0
    for i in range(n):
        tmp = min(a[i], b[i])
        if tmp > max:
            max = tmp
    total = sum(arr)
    s = max + (max * (max - 1))
    print(total - s)
