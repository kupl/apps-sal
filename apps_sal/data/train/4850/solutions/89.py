def solution(M1, M2, gm1, gm2, v, t):
    Mass1 = gm1 * 0.001 / M1
    Mass2 = gm2 * 0.001 / M2
    temp = t + 273.15
    return ((((Mass1 + Mass2) * 0.082) * temp) / v) * 1000
