import math


def get_grade(b, c, d):
    a = int((b + c + d) / 30)
    return 'A' if a == 10 else 'F' if a < 6 else chr(74 - a)
