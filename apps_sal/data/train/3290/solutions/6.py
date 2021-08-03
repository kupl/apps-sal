def get_ages(sum_, difference):
    x = (sum_ + difference) / 2
    y = sum_ - x
    return None if any(e < 0 for e in (x, y, sum_, difference)) else (x, y)
