for _ in range(int(input())):
    (n, k) = map(int, input().split())
    ls = list(map(int, input().split()))
    if n == 1:
        print('YES')
        print(1)
        continue
    if k == 1:
        print('NO')
        continue
    if k == 2 and n > 2:
        if ls[0] != ls[1] - 1:
            print('NO')
            continue
    print('YES')
    mx = n
    arr = [0] * n
    for i in range(ls[0] - 1):
        arr[i] = mx
        mx -= 1
    for i in range(ls[0], ls[1] - 1):
        arr[i] = mx
        mx -= 1
    for i in range(k - 1, -1, -1):
        arr[ls[i] - 1] = mx
        mx -= 1
    for i in range(1, n):
        if arr[i] == 0:
            arr[i] = mx
            mx -= 1
    print(*arr)
