def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    molar_mass1 = given_mass1 * 0.001 / molar_mass1
    molar_mass2 = given_mass2 * 0.001 / molar_mass2
    tempKelvin = temp + 273.15
    R = 0.082
    Ptotal = (molar_mass1 + molar_mass2) * R * tempKelvin / volume * 1000
    return Ptotal
