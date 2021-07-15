def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
    temp = temp + 273.15
    return ((n1 * 0.082 * temp) / volume) + ((n2 * 0.082 * temp) / volume)
