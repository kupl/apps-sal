def get_last_digit(index):
    if index <= 2:
        return 1
    (x, y) = (1, 1)
    for i in range(index - 2):
        res = x + y
        (x, y) = (y, res)
    return res % 10
