def sorter(textbooks):
    textbooks.sort()
    return sorted(textbooks, key=lambda x: x.lower())  # Cramming before a test can't be that bad?
