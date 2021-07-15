def flatten(lst):
    return sum(([i] if not isinstance(i, list) else i for i in lst), [])
