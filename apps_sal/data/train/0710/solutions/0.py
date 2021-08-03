def maxval(arr):
    fn = [float('-inf')] * (len(arr) + 1)
    sn = [float('-inf')] * len(arr)
    tn = [float('-inf')] * (len(arr) - 1)
    fon = [float('-inf')] * (len(arr) - 2)
    for i in reversed(list(range(len(arr)))):
        fn[i] = max(fn[i + 1], arr[i])
    for i in reversed(list(range(len(arr) - 1))):
        sn[i] = max(sn[i + 1], fn[i + 1] - arr[i])

    for i in reversed(list(range(len(arr) - 2))):
        tn[i] = max(tn[i + 1], sn[i + 1] + arr[i])

    for i in reversed(list(range(len(arr) - 3))):
        fon[i] = max(fon[i + 1], tn[i + 1] - arr[i])
    return fon[0]


n = int(input())
arr = list(map(int, input().split()))
print(maxval(arr))
