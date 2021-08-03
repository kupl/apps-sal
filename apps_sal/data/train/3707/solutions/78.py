def sorter(textbooks):
    # Cramming before a test can't be that bad?
    ts = sorted(textbooks, key=str.lower)
    return ts
