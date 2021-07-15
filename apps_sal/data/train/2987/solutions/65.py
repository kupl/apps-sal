def is_divide_by(number, a, b):
    bool = 0
    if number % a == 0:
        if number % b == 0:
            bool = 1
    return bool
