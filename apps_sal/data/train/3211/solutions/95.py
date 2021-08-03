def divide(weight):
    for i in range(2, weight + 1, 2):
        for j in range(2, weight + 1, 2):
            if i + j == weight:
                return True
    print(weight)
    return False
