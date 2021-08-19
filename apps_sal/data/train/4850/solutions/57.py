def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    total_mass = given_mass1 / molar_mass1 + given_mass2 / molar_mass2
    return total_mass * 0.082 * (temp + 273.15) / volume
