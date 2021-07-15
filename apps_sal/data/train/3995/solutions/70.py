def dating_range(age):
    if age < 15:
        return f'{int(0.9 * age)}-{int(1.1 * age)}'
    return f'{7 + age // 2}-{2 * (age - 7)}'
