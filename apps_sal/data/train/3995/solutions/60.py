from math import floor
def dating_range(age):
    return f"{age // 2 + 7}-{(age - 7) * 2}" if age > 14 else f"{floor(age - age / 10)}-{age + age // 10}"
