def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    mass1 = given_mass1 * .001 / molar_mass1
    mass2 = given_mass2 * .001 / molar_mass2
    newtemp = temp + 273.15
    return ((mass1 + mass2) * .082 * newtemp * 1000) / volume
