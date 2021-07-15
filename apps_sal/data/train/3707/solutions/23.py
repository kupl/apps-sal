def sorter(textbooks):
    k = sorted(textbooks, key=str.casefold)
    return k
