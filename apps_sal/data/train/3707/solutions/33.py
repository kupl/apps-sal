def sorter(textbooks):

    def f(x):
        return x.lower()
    return sorted(textbooks, key=f)
