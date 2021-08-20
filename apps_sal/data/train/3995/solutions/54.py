def dating_range(age):
    if age <= 14:
        return f'{int(age - age * 0.1)}-{int(age + age * 0.1)}'
    return f'{int(age / 2 + 7)}-{int((age - 7) * 2)}'
