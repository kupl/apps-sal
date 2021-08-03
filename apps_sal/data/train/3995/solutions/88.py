def dating_range(age):
    if age <= 14:
        min_ = age - 0.10 * age
        max_ = age + 0.10 * age
        return "{}-{}".format(int(min_), int(max_))
    if age > 14:
        min_ = (age / 2) + 7
        max_ = (age - 7) * 2
        return "{}-{}".format(int(min_), int(max_))
