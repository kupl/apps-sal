def dating_range(age):
    return "{}-{}".format(int(age - 0.1 * age) if age <= 14 else (age // 2) + 7, int(age + 0.1 * age) if age <= 14 else (age - 7) * 2)
