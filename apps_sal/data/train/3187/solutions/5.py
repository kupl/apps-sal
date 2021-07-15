def sum_nested(lst):
    if not isinstance(lst, list):
        return lst

    return sum(sum_nested(x) for x in lst)
