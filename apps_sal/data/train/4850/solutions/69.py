def solution(gmol1, gmol2, m1, m2, volume, temp):
    return (m1 / gmol1 + m2 / gmol2) * 0.082 * (temp + 273.15) / volume
