def get_ages(sum_, difference):
    a = (sum_ + difference) / 2
    b = sum_ - a
    if 0 <= b <= a:
        return (a, b)
