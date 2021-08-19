def positive_to_negative(b):
    return [int(d) for d in f"{int(''.join((str(1 - d) for d in b)), 2) + 1:b}"] if 1 in b else b
