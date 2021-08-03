def myf(a):
    return a.lower()


def sorter(textbooks):
    return sorted(textbooks, key=myf)
