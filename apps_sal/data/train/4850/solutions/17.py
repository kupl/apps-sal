def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    R = 0.082;
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
    num = (n1 + n2) * R * (temp + 273.15)
    return num / volume
