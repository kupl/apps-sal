def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
    return (n1 + n2) * 0.082 * (temp + 273.15) / volume
