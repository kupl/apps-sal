def divide(weight):
    length = weight - 1
    for n in range(1, weight):
        if n % 2 == 0 and length % 2 == 0 and n + length == weight:
            return True
        length -= 1
    return False
