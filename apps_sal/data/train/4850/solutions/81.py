R = 0.082


def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    # P = nRT/V
    # n = nr of mols
    # Ptotal = P1 + P2
    n = (given_mass1 / molar_mass1) + (given_mass2 / molar_mass2)
    T = temp + 273.15
    V = volume
    P = n * R * T / V
    return (P)
