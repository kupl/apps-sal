for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    st = set(arr)

    mex = -1

    for i in range(1, n + 1):
        if i not in st:
            mex = i
            break

    if mex == m:
        print(n)
    elif mex < m:
        print(-1)
    else:
        res = 0

        for i in arr:
            if i != m:
                res += 1

        print(res)
