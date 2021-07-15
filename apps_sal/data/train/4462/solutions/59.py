adjacent_element_product = lambda lst: max(x * y for x, y in zip(lst, lst[1:]))
