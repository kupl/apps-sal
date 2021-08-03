def max_product(lst, n):
    result = 1
    for number in sorted(lst)[-n:]:
        result *= number
    return result
