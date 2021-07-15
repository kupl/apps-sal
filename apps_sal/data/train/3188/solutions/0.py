def basereduct(x):
    for _ in range(150):
        x = int(str(x), int(max(str(x))) + 1 + ('9' in str(x)))
        if x < 10: return x
    return -1
