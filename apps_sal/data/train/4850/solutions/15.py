def solution(M1, M2, m1, m2, v, t):
    M1 = m1 * 0.001/M1
    M2 = m2 * 0.001/M2
    t = t + 273.15
    r = 0.082
    return (((M1 + M2) * r * t) / v) * 1000
