def largest_sum(arr):
    (ans, sum) = (0, 0)
    for i in range(len(arr)):
        sum = max(arr[i], arr[i] + sum)
        ans = max(ans, sum)
    return ans
