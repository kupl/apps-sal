def adjacent_element_product(array):
    res = []
    for i in range(len(array) - 1):
        ans = array[i] * array[i + 1]
        res.append(ans)
    return max(res)
