R = 0.082
CELSIUS_TO_KELVIN = 273.15


def solution(M1, M2, m1, m2, V, T):
    return ((m1 / M1 + m2 / M2) * R * (T + CELSIUS_TO_KELVIN)) / V
