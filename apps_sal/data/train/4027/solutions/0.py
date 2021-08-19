def sum_nested_numbers(a, depth=1):
    return sum((sum_nested_numbers(e, depth + 1) if type(e) == list else e ** depth for e in a))
