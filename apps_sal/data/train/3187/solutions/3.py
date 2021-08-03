def sum_nested(lst):
    return sum(map(sum_nested, lst)) if isinstance(lst, list) else lst
