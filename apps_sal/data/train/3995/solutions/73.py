from math import floor

def dating_range(age):
    if age <= 14:
        return f"{floor(0.9*age)}-{floor(1.1*age)}"
    return f"{age // 2 + 7}-{2*(age - 7)}"
