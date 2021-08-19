def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    pressure = (given_mass1 / molar_mass1 + given_mass2 / molar_mass2) * (temp + 273.15) * 0.082 / volume
    return pressure
