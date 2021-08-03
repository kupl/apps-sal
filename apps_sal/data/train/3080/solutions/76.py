def who_is_paying(name):
    trunc = name[:2]
    arr = [name, trunc]

    if len(name) < 3:
        arr.pop()
    return arr
