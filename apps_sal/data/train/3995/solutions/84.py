def dating_range(age):
    if age <= 14:
        msg = str(int(age * 0.9)) + '-' + str(int(age * 1.1))
    else:
        msg = str(int(age / 2) + 7) + '-' + str((age - 7) * 2)
    return msg
