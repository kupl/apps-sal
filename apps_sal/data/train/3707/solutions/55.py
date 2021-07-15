import locale

def sorter(textbooks):
    textbooks.sort(key=lambda x: x.lower())
    return textbooks
