def sorter(textbooks):
    textbooks = sorted(textbooks, key = str.casefold)
    return textbooks
