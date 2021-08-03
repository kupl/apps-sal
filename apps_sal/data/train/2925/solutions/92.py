def multiply(n):
    l = str(n)
    a = ""
    for c in l:
        if c in "0123456789":
            a += c

    return n * 5 ** len(a)
