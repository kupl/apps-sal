def dating_range(age, x=2, y=7, z=.1):
    return '%d-%d' % ((age / x + y, x * (age - y)) if age > x * y else (age * (1 - z), age * (1 + z)))
