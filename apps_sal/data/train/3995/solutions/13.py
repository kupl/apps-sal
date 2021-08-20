def dating_range(age):
    if age > 14:
        a = age / 2 + 7
        b = (age - 7) * 2
    else:
        a = age - 0.1 * age
        b = age + 0.1 * age
    return f'{int(a)}-{int(b)}'
