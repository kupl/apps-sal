def dating_range(age):
    return '%d-%d' % (age // 2 + 7, 2 * (age - 7)) if age > 14 else '%d-%d' % (9 * age // 10, 11 * age // 10)
