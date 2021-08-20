def sorter(textbooks):
    return sorted([textbook for textbook in textbooks], key=lambda x: x.lower())
