def has_unique_chars(str):
    return all((str.count(s) == 1 for s in str))
