"""
Answer => Combine Mass1 & Mass2, multiply by 0.082, multiply by Temperature, divide by the Volume, multiply by 1000
"""


def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    temp += 273.15

    m1 = given_mass1 * 0.001 / molar_mass1
    m2 = given_mass2 * 0.001 / molar_mass2

    return (m1 + m2) * 0.082 * temp / volume * 1000
