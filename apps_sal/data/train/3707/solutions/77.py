def sorter(textbooks):
    print(sorted(textbooks))
    return sorted(textbooks, key=lambda x: x.lower())
