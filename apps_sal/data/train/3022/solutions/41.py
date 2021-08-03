def two_highest(arg1):
    if len(arg1) <= 1:
        return arg1
    h1 = arg1[0]
    h2 = arg1[1]
    if h2 > h1:
        h1, h2 = h2, h1
    for i in range(2, len(arg1)):
        if arg1[i] > h1:
            h2 = h1
            h1 = arg1[i]
        elif arg1[i] > h2 and arg1[i] != h1:
            h2 = arg1[i]
    if h1 != h2:
        return [h1, h2]
    return [h1]
