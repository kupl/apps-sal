def dating_range(age):
    return "%d-%d" % (age // 2 + 7, (age - 7) * 2) if age > 14 else "%d-%d" % (int(age - 0.1 * age), int(age + 0.1 * age))
