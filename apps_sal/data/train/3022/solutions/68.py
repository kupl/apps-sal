def two_highest(arg1):
    unique = set(arg1)
    if len(unique) <= 2:
        return sorted(list(unique), reverse=True)
    max1 = max(unique)
    unique.discard(max1)
    max2 = max(unique)
    return [max1, max2]
