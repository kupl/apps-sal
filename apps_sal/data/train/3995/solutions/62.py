def dating_range(age):
    if age > 14:
        return str(int(age / 2 + 7)) + '-' + str((age - 7) * 2)
    else:
        return str(int(age - 0.1 * age)) + '-' + str(int(age + 0.1 * age))
