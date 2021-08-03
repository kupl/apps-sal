def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    temp += 273.15
    p1 = (given_mass1 / molar_mass1 * 0.082 * temp) / volume
    p2 = (given_mass2 / molar_mass2 * 0.082 * temp) / volume
    return p1 + p2
