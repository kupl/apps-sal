def divide(w):
    for i in range(2, w, 2):
        if (w - i) % 2 == 0:
            return True
    return False
