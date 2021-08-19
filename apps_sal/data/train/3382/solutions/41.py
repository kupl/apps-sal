def lowercase_count(strng):
    import re
    from re import finditer
    pattern = '[a-z]'
    count = 0
    for it in finditer(pattern, strng):
        count += 1
    return count
