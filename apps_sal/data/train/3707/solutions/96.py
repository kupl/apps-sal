def sorter(textbooks):
    # Cramming before a test can't be that bad?
    return sorted([textbook for textbook in textbooks], key=lambda x: x.lower())
