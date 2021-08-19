def is_tune(notes):
    if not notes:
        return False
    for j in range(12):
        if set(((i + j) % 12 for i in notes)).issubset({0, 2, 4, 5, 7, 9, 11}):
            return True
    return False
