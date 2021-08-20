def dating_range(age):
    return str(age // 2 + 7) + '-' + str((age - 7) * 2) if age > 14 else str(int(age - 0.1 * age)) + '-' + str(int(age + 0.1 * age))
