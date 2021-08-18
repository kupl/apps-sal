def sorter(textbooks):
    return sorted(textbooks, key=lambda x: x[0:2].lower())
