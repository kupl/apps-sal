def solution(gmol1, gmol2, m1, m2, volume, temp):
    # PV=nRT
    # n = n1 + n2
    # nx = gx / (g/mol)x
    return (m1 / gmol1 + m2 / gmol2) * 0.082 * (temp + 273.15) / volume
