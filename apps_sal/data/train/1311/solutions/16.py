for _ in range(int(input())):
    (n, k) = map(int, input().split())
    arr = []
    for i in range(n):
        if i % 2 == 0:
            arr.append(i + 1)
        else:
            arr.append(-i - 1)
    pos = n // 2 + n % 2
    neg = n // 2
    if k < pos:
        for i in range(n - 1, -1, -1):
            if k == pos:
                break
            if arr[i] > 0:
                arr[i] = -arr[i]
                pos -= 1
    else:
        for i in range(n - 1, -1, -1):
            if k == pos:
                break
            if arr[i] < 0:
                arr[i] = -arr[i]
                pos += 1
    print(*arr)
