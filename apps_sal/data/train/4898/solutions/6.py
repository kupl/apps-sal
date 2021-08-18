import re


def digit_all(x):
    try:
        return re.sub(r"[\D]", '', x)
    except TypeError:
        return "Invalid input !"
