def dating_range(age):
    return '{}-{}'.format(int(age * 0.9), int(age * 1.1)) if age <= 14 else '{}-{}'.format(int(age / 2 + 7), int((age - 7) * 2))
