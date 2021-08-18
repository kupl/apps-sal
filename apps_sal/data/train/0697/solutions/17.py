for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    pows = list(map(int, input().split()))
    if k == 1:
        print(max(pows))
        continue
    arr = []
    lastsum = None
    for i in range(n - k + 1):
        if lastsum is None:
            lastsum = sum(pows[:k])
            arr.append(lastsum)
        else:
            lastsum += pows[i + k - 1] - pows[i - 1]
            arr.append(lastsum)
    print(max(arr))
