def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    mass1 = given_mass1 / molar_mass1
    mass2 = given_mass2 / molar_mass2
    temp = temp + 273.15

    return (mass1 * 0.082 * temp / volume) + (mass2 * 0.082 * temp / volume)
