def is_divide_by(number, a, b):
    mod_a = number % a
    mod_b = number % b

    return mod_a == 0 and mod_b == 0
