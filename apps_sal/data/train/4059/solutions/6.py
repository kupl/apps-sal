def switch_lights(a):
    ones = a.count(1)
    for i, x in enumerate(a):
        if ones % 2:
            a[i] = 0 if x else 1
        ones -= x

    return a
