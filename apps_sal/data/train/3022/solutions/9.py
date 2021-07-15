def two_highest(arg1):
    return type(arg1) == list and sorted(list(set(arg1)), reverse=True)[:2]
