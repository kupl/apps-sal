def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    # Ideal gas law: P = nRT / V

    # Gas constant
    R = 0.082

    # Volume
    V = volume

    # Temperature
    T = temp + 273.15

    # Moles
    n_1 = given_mass1 / molar_mass1
    n_2 = given_mass2 / molar_mass2
    n_tot = n_1 + n_2

    # Pressure
    P = n_tot * R * T / V

    return P
