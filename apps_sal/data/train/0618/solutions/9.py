def maxSum(arr, n, k):

    total = sum(arr[:k])

    x = total
    for i in range(k, n):
        x += arr[i] - arr[i - k]
        total = max(total, x)
    return total


for _ in range(int(input())):
    n, k = map(int, input().split())

    li = [int(i) for i in input().split()] * 2
    print(maxSum(li, 2 * n, k))
