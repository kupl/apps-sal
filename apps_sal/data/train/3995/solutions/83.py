from math import floor

def dating_range(age):
    if age <= 14:
        return f'{floor(age * 0.9)}-{floor(age * 1.1)}'
    else:
        return f'{floor(age / 2 + 7)}-{floor((age - 7) * 2)}'

