def dating_range(age):
    if age > 14:
        a = int(age / 2 + 7)
        b = (age - 7) * 2
    else:
        a = int(age - 0.10 * age)
        b = int(age + 0.10 * age)

    return f'{min(a, b)}-{max(a, b)}'
