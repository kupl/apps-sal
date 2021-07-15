def solution(M1, M2, m1, m2, V, T):
    t = T + 273.15
    return 0.082 * (m1/M1 + m2/M2) * t / V
