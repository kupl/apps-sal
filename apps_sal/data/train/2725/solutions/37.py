def gimme(b):
    a = max(b[0], b[1], b[2])
    c = min(b[0], b[1], b[2])
    for i in range(3):
        if b[i] != a and b[i] != c:
            return i
