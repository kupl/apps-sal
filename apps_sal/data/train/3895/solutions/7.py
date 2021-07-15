def shifted_diff(first, second):
    if len(first) != len(second):
        return -1
    return (second * 2).find(first)
