def digitize(n):
    new = []
    for I in str(n):
        new.append(int(I))
    return new[::-1]
