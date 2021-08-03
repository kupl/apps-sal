def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    n1 = given_mass1 / (1000 * molar_mass1)
    n2 = given_mass2 / (1000 * molar_mass2)
    return 0.082 * (n1 + n2) * (temp + 273.15) / (volume / 1000)
