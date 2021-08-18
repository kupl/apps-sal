from math import log2

ns = ["A", "A


def get_note(p):
    return ns[round(log2(p / 55) * 12) % 12]
