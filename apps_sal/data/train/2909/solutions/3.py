def is_tune(notes):
    pattern = [0, 2, 4, 5, 7, 9, 11]
    if notes:
        for i in range(12):
            for n in notes:
                for p in pattern:
                    if (i - n + p) % 12 == 0:
                        break
                else:
                    break
            else:
                return True
    return False
