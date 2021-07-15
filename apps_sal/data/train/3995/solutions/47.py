def dating_range(age):
    k = (age*0.5 + 7, age*2 - 14) if age > 14 else (age - 0.1 * age, age + 0.1 * age)
    return '{}-{}'.format(int(k[0]), int(k[1]))
