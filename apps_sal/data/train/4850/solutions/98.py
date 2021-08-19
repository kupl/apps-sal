def solution(mm1, mm2, gm1, gm2, volume, temp):
    # your code goes here
    R = 0.082
    return R * (gm1 / mm1 + gm2 / mm2) * (temp + 273.15) / volume
