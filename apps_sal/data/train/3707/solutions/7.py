def sorter(textbooks):
    def f(e):
        return e.lower()
    sorted = textbooks.sort(key=f)
    return textbooks
