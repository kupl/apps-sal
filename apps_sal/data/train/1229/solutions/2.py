for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    arr = [int(k) for k in input().split()]
    motu = []
    tomu = []
    for i in range(n):
        if i % 2 == 0:
            motu.append(arr[i])
        else:
            tomu.append(arr[i])
    motu.sort(reverse=True)
    tomu.sort()
    for i in range(len(motu)):
        if len(tomu) - 1 < i:
            break
        if k == 0:
            break
        if tomu[i] < motu[i]:
            temp = tomu[i]
            tomu[i] = motu[i]
            motu[i] = temp
            k -= 1
    sumtomu = 0
    summotu = 0
    for i in range(len(tomu)):
        sumtomu += tomu[i]
    for i in range(len(motu)):
        summotu += motu[i]
    if sumtomu > summotu:
        print('YES')
    else:
        print('NO')
