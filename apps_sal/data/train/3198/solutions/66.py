def check_exam(a1, a2):
    s = 0
    for (x, z) in zip(a1, a2):
        if not z:
            pass
        elif x == z:
            s += 4
        else:
            s -= 1
    return s if s >= 0 else 0
