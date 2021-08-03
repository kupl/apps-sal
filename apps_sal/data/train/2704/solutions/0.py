def almost_increasing_sequence(sequence):
    save, first = -float('inf'), True
    for i, x in enumerate(sequence):
        if x > save:
            save = x
        elif first:
            if i == 1 or x > sequence[i - 2]:
                save = x
            first = False
        else:
            return False
    return True
