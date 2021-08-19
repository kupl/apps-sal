def capitalize(s):
    f1 = ''
    f2 = ''
    result = []
    for (i, v) in enumerate(s):
        if i == 0 or i % 2 == 0:
            f1 += v.upper()
        else:
            f1 += v.lower()
    result.append(f1)
    for (j, v) in enumerate(s):
        if j == 0 or j % 2 == 0:
            f2 += v.lower()
        else:
            f2 += v.upper()
    result.append(f2)
    return result
