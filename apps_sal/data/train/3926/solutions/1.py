import re


def check_root(string):
    if not re.fullmatch(r"(-?\d+,){3}-?\d+", string):
        return 'incorrect input'
    a, b, c, d = list(map(int, string.split(",")))
    if not d == c + 1 == b + 2 == a + 3:
        return 'not consecutive'
    return f"{a * b * c * d + 1}, {abs(b ** 2 + a)}"
