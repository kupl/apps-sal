def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    P1 = ((given_mass1 / molar_mass1) * 0.082 * (temp + 273.15)) / volume
    P2 = ((given_mass2 / molar_mass2) * 0.082 * (temp + 273.15)) / volume
    P_total = P1 + P2
    return P_total
