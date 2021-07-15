def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    M1 = given_mass1 * 0.001 / molar_mass1
    M2 = given_mass2 * 0.001 / molar_mass2
    temp = temp + 273.15
    R = 0.082
    return (((M1 + M2) * R * temp) / volume) * 1000
