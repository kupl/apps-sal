def find_missing_number(numbers):
    s = set(numbers)
    m = max(s, default=0)
    try:
        return (set(range(1, m)) - s).pop()
    except KeyError:
        return m + 1
