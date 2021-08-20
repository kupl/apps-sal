def divide(weight):
    weightx = weight - 2
    if weightx <= 0:
        return False
    if weightx / 2 == weightx // 2:
        return True
    else:
        return False
