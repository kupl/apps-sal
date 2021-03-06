import sys


def maximum_subarray_sum(arr, n, k):
    if k == 1:
        return kadane(arr)
    one_sum = sum(arr)
    a = arr + arr
    if one_sum > 0:
        return kadane(a) + (k - 2) * one_sum
    return kadane(a)


def kadane(a):
    best_sum = float('-inf')
    curr_sum = 0
    for i in a:
        curr_sum = curr_sum + i
        best_sum = max(best_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return best_sum


def __starting_point():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    ans = []
    j = 1
    t = data[0]
    for i in range(t):
        n = data[j]
        k = data[j + 1]
        arr = data[j + 2:j + 2 + n]
        ans.append(maximum_subarray_sum(arr, n, k))
        j = j + 2 + n
    for x in ans:
        print(x)


__starting_point()
