def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    R = 0.082  # Gas constant
    T = temp + 273.15  # Kelvin
    n1 = given_mass1 / molar_mass1  # Amount of substance 1
    n2 = given_mass2 / molar_mass2  # Amount of substance 2
    return (n1 + n2) * R * T / volume
