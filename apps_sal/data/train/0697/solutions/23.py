def maxSum(arr, n, k):
    if (n < k):

        print("Invalid")
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
    n, k = [int(x) for x in input().split()]
    arr = list(map(int, input().split()))
    print(maxSum(arr, n, k))
