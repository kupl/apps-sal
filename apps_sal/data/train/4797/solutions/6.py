def shorter_reverse_longer(a, b):
    if len(a) >= len(b):
        (shorter, longer) = (b, a)
    else:
        (shorter, longer) = (a, b)
    return shorter + longer[::-1] + shorter
