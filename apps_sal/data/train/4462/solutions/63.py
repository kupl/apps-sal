def adjacent_element_product(lst):
    return max((a * b for (a, b) in zip(lst[:-1], lst[1:])))
