def dating_range(age):
    if age > 14:
        return str(age // 2 + 7) + '-' + str((age - 7) * 2)
    else:
        return (str(int(age * 0.9)) + '-' + str(int(age * 1.1)))
