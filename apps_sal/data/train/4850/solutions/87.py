def kelv_t(x):
    return x + 273.15


r = 0.082


def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    return r * kelv_t(temp) / volume * (given_mass1 / molar_mass1 + given_mass2 / molar_mass2)
