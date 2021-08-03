def dating_range(age):
    if age <= 14:
        min = int(age - age / 10)
        max = int(age + age / 10)
    else:
        min = int(age / 2 + 7)
        max = int(2 * (age - 7))
    return "{}-{}".format(min, max)
