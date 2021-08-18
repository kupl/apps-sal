def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):

    R = 0.082

    V = volume

    T = temp + 273.15

    n_1 = given_mass1 / molar_mass1
    n_2 = given_mass2 / molar_mass2
    n_tot = n_1 + n_2

    P = n_tot * R * T / V

    return P
