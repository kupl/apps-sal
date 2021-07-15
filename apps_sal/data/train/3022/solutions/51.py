def two_highest(arg1):
    return sorted(list(dict.fromkeys(arg1)), reverse=True)[:2]
