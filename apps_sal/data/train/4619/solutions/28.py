def whoseMove(x, y, b='black', w='white'):
    return x if y else w if x == b else b
