def lowercase_count(lst):
    """
    Count lowercase letters in a string.
    """
    n = 0
    for s in lst:
        if s >= 'a' and s <= 'z':
            n = n + 1
    return n
