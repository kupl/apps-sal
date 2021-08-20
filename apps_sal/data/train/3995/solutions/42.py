def dating_range(age):
    min_age = int(age / 2 + 7)
    max_age = int((age - 7) * 2)
    return age >= 14 and f'{min_age}-{max_age}' or f'{int(age - 0.1 * age)}-{int(age + 0.1 * age)}'
