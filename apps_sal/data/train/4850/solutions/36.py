def solution(M1, M2, m1, m2, V, T, R=0.082) :
    return R * (T + 273.15) * (m1 / M1 + m2 / M2) / V
