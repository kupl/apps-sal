def sorter(textbooks):
    a = sorted(textbooks, key=str.casefold)
    print(textbooks, a)
    return a
