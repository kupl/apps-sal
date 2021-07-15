R = .082
zK = 273.15

def solution(m1, m2, M1, M2, V, T):
    return (M1 / m1 + M2 / m2) * R * (T + zK) / V
