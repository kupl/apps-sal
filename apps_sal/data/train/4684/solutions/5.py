def is_hollow(x):
    if len(x) < 3:
        return False
    z = 0
    for i, (a, b) in enumerate(zip(x, x[::-1])):
        if i > len(x) // 2:
            return z >= 2
        if (a == 0) != (b == 0):
            return False
        if a != 0 and z > 0:
            return False
        if a == 0:
            z += 1
        elif z > 0:
            return False
