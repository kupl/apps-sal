import math


def find_closest_value(Q):
    B = math.ceil((math.ceil(Q / 65) / 2) ** 0.5)
    (S, B) = (130 * B * B, 65 * B)
    return S - min((0, B - 4, B + B - 13, 3 * B - 69, 4 * B - 130), key=lambda V: abs(Q - S + V)) or 4
