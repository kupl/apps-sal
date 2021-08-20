def dating_range(age):
    if age > 14:
        min = age / 2 + 7
        max = (age - 7) * 2
    elif age <= 14:
        min = age - 0.1 * age
        max = age + 0.1 * age
    return f'{int(min)}-{int(max)}'
