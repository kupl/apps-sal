def maximum_product_of_parts(number):
    (s, n, result) = (str(number), len(str(number)), 0)
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            (start, middle, end) = (s[0:i], s[i:j], s[j:])
            result = max(result, int(start) * int(middle) * int(end))
    return result
