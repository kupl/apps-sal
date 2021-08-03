def pressure(molar_mass, given_mass, v, t):
    return given_mass * 0.082 * (t + 273.15) / molar_mass / v


def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    return pressure(molar_mass1, given_mass1, volume, temp) + \
        pressure(molar_mass2, given_mass2, volume, temp)
