def arr(n=None): # None for if no arguments passed
    # [ the numbers 0 to N-1 ]
    a = []
    if n is None:
        return a
    else:
        for i in range(n):
            a.append(i)
        return a
