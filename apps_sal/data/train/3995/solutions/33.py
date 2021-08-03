def dating_range(age):
    min_over = age // 2 + 7
    max_over = (age - 7) * 2
    min_under = int(age - 0.10 * age)
    max_under = int(age + 0.10 * age)
    return f'{min_over}-{max_over}' if age > 14 else f'{min_under}-{max_under}'
