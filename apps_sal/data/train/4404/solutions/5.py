def compare(s1, s2):
    s1 = list(map(int, s1.split('.')))
    s2 = list(map(int, s2.split('.')))
    dif = abs(len(s1) - len(s2))
    s1.extend([0] * dif) if len(s1) < len(s2) else s2.extend([0] * dif)
    for val_1, val_2 in zip(s1, s2):
        if val_1 != val_2:
            return 1 if val_1 > val_2 else -1
    return 0
