from math import floor

def dating_range(age):
    min = floor(age / 2 + 7) if age > 14 else floor(age - 0.1 * age)
    max = floor((age - 7) * 2) if age > 14 else floor(age + 0.1 * age)
    return f"{min}-{max}"
