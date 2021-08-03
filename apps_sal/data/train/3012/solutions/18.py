def shared_bits(a, b):
    counter = 0
    for x in range(0, max(a, b) + 1):
        if a & pow(2, x) and b & pow(2, x):
            counter += 1
            if counter >= 2:
                return True
    return False
