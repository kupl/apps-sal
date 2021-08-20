def add(lst):
    if not isinstance(lst, list):
        return 'Invalid input'
    (total, result) = (0, [])
    for n in lst:
        if not isinstance(n, int):
            return 'Invalid input'
        total += n
        result.append(total)
    return result
