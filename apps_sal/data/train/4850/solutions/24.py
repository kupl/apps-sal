def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    R = 0.082
    return (given_mass1 / molar_mass1) * R * (temp + 273.15) / volume + (given_mass2 / molar_mass2) * R * (temp + 273.15) / volume
