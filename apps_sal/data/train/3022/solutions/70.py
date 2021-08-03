def two_highest(arg1):
    distinct = list(set(arg1))
    return sorted(distinct, reverse=True)[:2]
