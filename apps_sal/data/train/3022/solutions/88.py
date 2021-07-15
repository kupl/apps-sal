def two_highest(arg1):
    uniques = set(arg1)
    if len(uniques) <= 2:
        return sorted(uniques, reverse=True)
    return sorted(uniques, reverse=True)[:2]
