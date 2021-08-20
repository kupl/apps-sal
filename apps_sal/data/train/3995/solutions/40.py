def dating_range(age):
    if age > 12:
        return str(int(age / 2 + 7)) + '-' + str(int((age - 7) * 2))
    else:
        return str(int(age - 0.1 * age)) + '-' + str(int(age + 0.1 * age))
