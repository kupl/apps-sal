kelv_t = lambda x: x + 273.15
r = 0.082
solution = lambda molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp: r * kelv_t(temp) / volume * (given_mass1/molar_mass1 + given_mass2/molar_mass2)
