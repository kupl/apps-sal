def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    n_moles = given_mass1 / molar_mass1 + given_mass2 / molar_mass2

    r_constant = 0.082
    temp_kelvin = 273.15 + temp

    pressure = (r_constant * n_moles * temp_kelvin) / volume

    return pressure

    # your code goes here
