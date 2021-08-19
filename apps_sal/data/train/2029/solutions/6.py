n = int(input())
if n % 2 == 0:
    print('NO')
else:
    print('YES')
    sum = 2 * n + 1
    arr = [0] * 2 * n
    arr[0] = 1
    arr[2 * n - 1] = 2 * n
    i = 0
    for k in range(2, n + 1):
        if arr[(i + n) % (2 * n)] == 0:
            i = (i + n) % (2 * n)
            arr[i] = k
            arr[2 * n - 1 - i] = sum - k
        else:
            i = i + 1
            arr[i] = k
            arr[2 * n - 1 - i] = sum - k
    for x in arr:
        print(x, end=' ')
