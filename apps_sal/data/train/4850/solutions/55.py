def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    return (float(given_mass1) / float(molar_mass1) + float(given_mass2) / float(molar_mass2)) * 0.082 * (float(temp) + 273.15) / float(volume)
