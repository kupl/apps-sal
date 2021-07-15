def dating_range(age):
    min, max = (age / 2.0) + 7, (age - 7) * 2.0
    if age <= 14:
        min, max = age - 0.10 * age, age + 0.10 * age
    return "{}-{}".format(int(min), int(max))
