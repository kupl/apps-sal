def max_multiple(divisor, bound):
    ans = []
    for x in range(1, bound + 1):
        if x % divisor == 0:
            ans.append(x)
    return ans[-1]
