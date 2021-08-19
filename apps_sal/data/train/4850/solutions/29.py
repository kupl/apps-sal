def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    m1 = given_mass1 * 0.001 / molar_mass1
    m2 = given_mass2 * 0.001 / molar_mass2
    t = temp + 273.15
    R = 0.082
    p = (m1 + m2) * R * t / volume * 1000
    return p
