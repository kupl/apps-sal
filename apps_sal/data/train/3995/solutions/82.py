def dating_range(age):
    min = int((age / 2) + 7)
    max = int((age - 7) * 2)
    small_min = int(age - 0.10 * age)
    small_max = int(age + 0.10 * age)
    return str(min) + "-" + str(max) if age > 14 else str(small_min) + "-" + str(small_max)
