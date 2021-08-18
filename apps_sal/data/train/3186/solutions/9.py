def similarity(a, b):

    x = list(set(a + b))
    z = [num for num in a if num in a and num in b]
    try:
        return len(z) / len(x)
    except ZeroDivisionError:
        return 0
