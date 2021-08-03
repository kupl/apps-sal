def between(a, b):
    arr = [a]
    while a < b:
        arr.append(a + 1)
        a += 1
    return arr
