def multiple_of_index(a):
    l= []
    for i, v in enumerate(a):
        if i >= 1 and v%i == 0:
            l.append(v)
    return l

