for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    mx = sum(arr[0:min(k, n)])
    curr = mx
    for i in range(0, n - k):
        curr += arr[i + k] - arr[i]
        mx = max(mx, curr)
    print(mx)
