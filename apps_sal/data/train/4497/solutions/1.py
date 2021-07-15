def positive_to_negative(b):
    last = next((i for i in range(len(b) - 1, -1, -1) if b[i]), 0)
    return [1 - d for d in b[:last]] + b[last:]
