def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    mass_1 = given_mass1 / molar_mass1
    mass_2 = given_mass2 / molar_mass2
    temperature = temp + 273.15
    return (mass_1 + mass_2) * 0.082 * temperature / volume
