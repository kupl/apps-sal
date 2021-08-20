def dating_range(age):
    min_age = age // 2 + 7 if age > 14 else 9 * age // 10
    max_age = 2 * (age - 7) if age > 14 else 11 * age // 10
    return f'{min_age}-{max_age}'
