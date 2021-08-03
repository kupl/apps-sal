def multiply(n):

    l = len(str(n))
    lm = len(str(n)) - 1

    if str(n).startswith('-'):
        return n * 5**lm
    else:
        return n * 5**l
