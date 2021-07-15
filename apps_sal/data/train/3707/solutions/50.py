def f(x):
    x = x.lower()
    return x

def sorter(textbooks):
    textbooks.sort(key = f)
    return textbooks
