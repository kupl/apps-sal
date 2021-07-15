def solution(M1, M2, m1, m2, v, t):
    R = 0.082
    t += 273.15
    return m1*R*t/(M1*v) + m2*R*t/(M2*v)
