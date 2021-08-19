def maxCircularSum(arr, n, k):
    sum = 0
    start = 0
    end = k - 1
    for i in range(k):
        sum += arr[i]
    ans = sum
    for i in range(k, n + k):
        sum += arr[i % n] - arr[(i - k) % n]
        if sum > ans:
            ans = sum
            start = (i - k + 1) % n
            end = i % n
    return ans


for _ in range(int(input())):
    (n, k) = map(int, input().split())
    l = list(map(int, input().split()))
    print(maxCircularSum(l, n, k))
