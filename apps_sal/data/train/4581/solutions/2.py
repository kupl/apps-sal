def are_similar(a, b):
    c = [a[i] - b[i] for i in range(len(a)) if a[i] != b[i]]
    return c == [] or (len(c) == 2 and c[0] + c[1] == 0)
