
def two_highest(arg1):
    return (list(dict.fromkeys(sorted(arg1)))[-2:])[::-1]

