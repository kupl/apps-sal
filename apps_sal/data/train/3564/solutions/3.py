def stringy(size):
    s = ""
    for x in range (0, size):
        s+= str("1") if x%2 == 0 else str("0")
    return s
