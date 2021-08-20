def maxSum(arr, n, k):
    res = 0
    for i in range(k):
        res += arr[i]
    curr_sum = res
    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]
        res = max(res, curr_sum)
    return res


for i in range(int(input())):
    (n, k) = map(int, input().split())
    arr = list(map(int, input().split()))
    print(maxSum(arr, n, k))
