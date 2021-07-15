def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    m1 = given_mass1 * 0.001 / molar_mass1
    m2 = given_mass2 * 0.001 / molar_mass2
    T = temp + 273.15
    return (m1 + m2) * 0.082 * T / volume * 1000
