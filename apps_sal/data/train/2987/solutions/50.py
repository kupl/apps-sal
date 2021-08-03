def is_divide_by(number, a, b):
    x = number / a
    y = number / b
    if isinstance(x, int) and isinstance(y, int):
        return True
    else:
        try:
            float(x)
            float(y)
        except ValueError:
            return False
        else:
            return float(x).is_integer() and float(y).is_integer()
