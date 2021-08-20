def solution(mm1, mm2, gm1, gm2, v, t):
    return (gm1 / mm1 + gm2 / mm2) * (t + 273.15) * 0.082 / v
