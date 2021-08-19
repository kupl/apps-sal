def divide(weight):
    i = 1
    while i != weight:
        if i % 2 == 0 and (weight - i) % 2 == 0:
            return True
            break
        else:
            i += 1
    else:
        return False
