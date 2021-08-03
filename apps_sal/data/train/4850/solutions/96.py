def solution(M1, M2, m1, m2, V, T):
    M1 = m1 * 0.001 / M1
    M2 = m2 * 0.001 / M2
    T = T + 273.15
    return (((M1 + M2) * 0.082 * T) / V) * 1000
