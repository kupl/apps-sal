def solution(M1, M2, m1, m2, v, t):
    return ((m1 / M1) + (m2 / M2)) * 0.082 * (t + 273.15) / v
