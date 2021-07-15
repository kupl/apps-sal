def is_tune(notes):
    if not notes:
        return False
    c = 0
    print(notes)
    for i in range(len(notes)):
        for j in range(len(notes)):
            if (notes[j] - notes[i]) % 12 in [0, 1, 3, 5, 6, 8, 10]:
                c += 1
            else:
                c = 0
                break
        if c == len(notes):
            return True
    return False
