def dating_range(age):
    return ['%d-%d' % (age - 0.1 * age, age + 0.1 * age), '%d-%d' % (age / 2 + 7, (age - 7) * 2)][age > 14]
