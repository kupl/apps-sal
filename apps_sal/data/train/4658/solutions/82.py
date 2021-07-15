def max_product(lst, n_largest_elements):
    """
    Return the maximum product of k integers from lst.
    """
    lst = sorted(lst)
    res = 1
    for i in lst[-n_largest_elements:]:
        res *= i
    return res
