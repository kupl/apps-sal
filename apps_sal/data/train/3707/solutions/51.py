def sorter(textbooks):
    textbooks = sorted(textbooks, key=lambda x:x[0:] if x[0:].islower() else x[0:].lower())
    return textbooks
