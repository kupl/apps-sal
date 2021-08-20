def sorter(textbooks):
    textbooks.sort()
    return sorted(textbooks, key=lambda x: x.lower())
