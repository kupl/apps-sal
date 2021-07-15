def register(textbook):
    return textbook.lower()

def sorter(textbooks):
    textbooks.sort(key=register)
    return textbooks
