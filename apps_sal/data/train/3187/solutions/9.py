def sum_nested(lst):
    return sum(sum_nested(e) if type(e) is list else e for e in lst)
