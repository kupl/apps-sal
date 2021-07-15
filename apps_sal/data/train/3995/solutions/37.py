def dating_range(age):
    if age <= 14:
        return f'{int(age * 0.9)}-{int(age * 1.1)}'
    return f'{age // 2 + 7}-{(age - 7) * 2}'
