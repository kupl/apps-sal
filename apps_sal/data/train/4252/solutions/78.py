def merge_arrays(first, second):
    x = first + second
    y = []
    for i in x:
        if i in y:
            continue
        else:
            y.append(i)
    y.sort()
    return y
