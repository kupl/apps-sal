from math import ceil


def balanced_num(number):
    if number < 100:
        return "Balanced"
    digits = [int(ch) for ch in str(number)]
    middle = ceil(len(digits) / 2) - 1
    return "Balanced" if sum(digits[:middle]) == sum(digits[-middle:]) else "Not Balanced"
