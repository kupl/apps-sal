def sorter(textbooks):
    return sorted(set(textbooks), key=str.casefold)
