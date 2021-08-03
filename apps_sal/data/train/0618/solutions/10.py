# cook your dish here
def maxCircularSum(arr, n, k):

    # k must be greater

    sum = 0
    start = 0
    end = k - 1

    # calculate the sum of first k elements.
    for i in range(k):
        sum += arr[i]

    ans = sum

    for i in range(k, n + k):

        # add current element to sum
        # and subtract the first element
        # of the previous window.
        sum += arr[i % n] - arr[(i - k) % n]

        if (sum > ans):
            ans = sum
            start = (i - k + 1) % n
            end = i % n

    return ans


# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    print(maxCircularSum(l, n, k))
