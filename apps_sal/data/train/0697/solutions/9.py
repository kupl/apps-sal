def maxSum(arr, n, k):
    if n < k:
        print('Invalid')
        return -1
    res = 0
    for i in range(k):
        res += arr[i]
    curr_sum = res
    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]
        res = max(res, curr_sum)
    return res


for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    print(maxSum(l, n, k))
