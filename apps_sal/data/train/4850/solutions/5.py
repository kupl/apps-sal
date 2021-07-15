def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    temp += 273.15
    R = 0.082
    n = given_mass1/molar_mass1 + given_mass2/molar_mass2
    return n*R*temp/volume
