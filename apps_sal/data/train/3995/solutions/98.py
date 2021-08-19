def dating_range(age):
    r = (age - 0.1 * age, age + 0.1 * age)
    if age > 14:
        r = (age / 2 + 7, (age - 7) * 2)
    return '{}-{}'.format(int(r[0]), int(r[1]))
