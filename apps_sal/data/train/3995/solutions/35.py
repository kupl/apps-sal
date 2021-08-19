def dating_range(age):
    if age >= 15:
        min_age = int(age / 2 + 7)
        max_age = (age - 7) * 2
    else:
        min_age = int(age - 0.1 * age)
        max_age = int(age + 0.1 * age)
    return f'{min_age}-{max_age}'
