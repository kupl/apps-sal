def dating_range(age):
    if age <= 14:
        min_age = int(age - 0.1 * age)
        max_age = int(age + 0.1 * age)
    else:
        min_age = int(age / 2 + 7)
        max_age = int((age - 7) * 2)
    return f"{min_age}-{max_age}"
