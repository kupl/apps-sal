def divide(w):
    if w > 2:
        w2 = w % 2
        return w2 % 2 == 0
    else:
        return False
