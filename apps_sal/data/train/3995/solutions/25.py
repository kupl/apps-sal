def dating_range(age):
    if age > 14:
        min = int(age / 2 + 7)
        max = int((age - 7) * 2)
    else:
        min = int(age - 0.1 * age)
        max = int(age + 0.1 * age)
    r = str(min)
    r += '-'
    r += str(max)
    return r
