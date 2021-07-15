def two_highest(arg1):
    print(sorted(list(set(arg1)), reverse=True))
    return sorted(list(set(arg1)), reverse=True)[:2]
