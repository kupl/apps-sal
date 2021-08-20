def get_last_digit(index):
    (a, b) = (0, 1)
    for i in range(index):
        (a, b) = (b, (a + b) % 10)
    return a
