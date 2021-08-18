for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    res = (arr[0] - 1) // k
    for i in range(1, len(arr)):
        res += (arr[i] - arr[i - 1] - 1) // k
    print(res)
