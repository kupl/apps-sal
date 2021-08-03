def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    mass1 = given_mass1 * 0.001 / molar_mass1
    mass2 = given_mass2 * 0.001 / molar_mass2
    combined_mass = mass1 + mass2
    kelvin = temp + 273.15
    return combined_mass * 0.082 * kelvin / volume * 1000
