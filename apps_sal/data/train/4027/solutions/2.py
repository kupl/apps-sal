def sum_nested_numbers(a, lvl=0):
    return a ** lvl if not isinstance(a, list) else sum((sum_nested_numbers(b, lvl + 1) for b in a))
