def dating_range(y):
    """
    rename or delete
    """
    return str(y // 2 + 7) + '-' + str(2 * (y - 7)) if y > 14 else str(int(0.9 * y)) + '-' + str(int(1.1 * y))
