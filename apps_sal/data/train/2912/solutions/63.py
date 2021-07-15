def find_multiples(integer, limit):
    ans = []
    for i in range(1, limit//integer + 1):
        ans.append(integer*i)
    return ans
