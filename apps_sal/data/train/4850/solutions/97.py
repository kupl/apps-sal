def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    R = 0.082
    Mass1 = given_mass1 / molar_mass1
    Mass2 = given_mass2 / molar_mass2
    return (Mass1 + Mass2) * R / volume * (temp + 273.15)
