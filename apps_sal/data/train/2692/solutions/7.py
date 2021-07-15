def bubble(l):
    output, toChange = [], True
    while toChange:
        toChange = False
        for i, x in enumerate(l[:-1]):
            if l[i + 1] < l[i]:
                l[i], l[i + 1] = l[i + 1], l[i]
                output.append(l[:])
                toChange = True
    return output
