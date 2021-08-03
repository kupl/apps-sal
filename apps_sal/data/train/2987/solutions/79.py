def is_divide_by(number, a, b):
    from math import fmod
    return sum([fmod(number, float(a)), fmod(number, float(b))]) == 0.0
