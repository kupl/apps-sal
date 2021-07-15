def sorter(textbooks):
    return sorted(sorted(textbooks, key = lambda x: x[1].lower()), key = lambda x: x[0].lower())
