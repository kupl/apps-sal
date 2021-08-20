def get_ages(a, b):
    x = (a + b) / 2
    y = (a - b) / 2
    return None if a < 0 or b < 0 or x < 0 or (y < 0) else (x, y)
