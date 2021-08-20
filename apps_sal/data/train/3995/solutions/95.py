def dating_range(age):
    if age > 14:
        min = age // 2 + 7
        max = (age - 7) * 2
        return f'{min}-{max}'
    else:
        min = int(age - 0.1 * age)
        max = int(age + 0.1 * age)
        return f'{min}-{max}'
