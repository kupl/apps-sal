def adjacent_element_product(lst): return max(x * y for x, y in zip(lst, lst[1:]))
