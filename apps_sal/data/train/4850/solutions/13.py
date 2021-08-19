def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
    R = 0.082
    T = temp + 273.15
    V = volume
    P = (n1 + n2) * R * T / V
    return P
