def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    pressure_1 = given_mass1 / molar_mass1 * 0.082 * (temp + 273.15) / volume
    pressure_2 = given_mass2 / molar_mass2 * 0.082 * (temp + 273.15) / volume
    return pressure_1 + pressure_2
