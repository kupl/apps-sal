def sum_of_minimums(numbers):
    ans = 0
    for arr in numbers:
        ans += min(arr)
    return ans
