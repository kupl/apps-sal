def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    R = 0.082
    P1 = R * given_mass1 / molar_mass1 * (temp + 273.15) / volume
    P2 = R * given_mass2 / molar_mass2 * (temp + 273.15) / volume
    return P1 + P2
