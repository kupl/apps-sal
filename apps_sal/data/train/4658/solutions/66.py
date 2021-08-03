def max_product(lst, n_largest_elements):
    sort = sorted(lst)
    res = []
    for i in range(n_largest_elements):
        res.append(sort.pop())
    ans = 1
    for num in res:
        ans *= num
    return ans
