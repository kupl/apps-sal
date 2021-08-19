def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    R = 0.082
    T = temp + 273.15
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
    return (n1 + n2) * R * T / volume
