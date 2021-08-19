try:

    def maxSum(arr, n, k):
        res = 0
        for i in range(k):
            res += arr[i]
        curr_sum = res
        for i in range(k, n):
            curr_sum += arr[i] - arr[i - k]
            res = max(res, curr_sum)
        return res
    t = int(input())
    for _ in range(t):
        (n, k) = map(int, input().split())
        arr = list(map(int, input().split()))
        arr = arr + arr[:k - 1]
        n1 = len(arr)
        print(maxSum(arr, n1, k))
except:
    pass
