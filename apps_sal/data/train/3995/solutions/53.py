def dating_range(age):
    import math
    if age <= 14:
        return f'{math.floor(age - 0.1 * age)}-{math.floor(age + 0.1 * age)}'
    else:
        return f'{math.floor(age / 2 + 7)}-{math.floor(2 * (age - 7))}'
