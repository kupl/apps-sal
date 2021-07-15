def dating_range(age):
    if age <= 14:
        min = age - age / 10
        max = age + age / 10
    else:
        min = age / 2 + 7
        max = 2 * (age - 7)
    return "%d-%d" % (int(min), int(max))
