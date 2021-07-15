def two_highest(lst):
    return isinstance(lst, list) and sorted(set(lst), reverse = 1)[:2]
