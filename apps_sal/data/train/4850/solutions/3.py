def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    t = temp + 273.15
    R = 0.082
    n_mol1 = given_mass1 / molar_mass1
    n_mol2 = given_mass2 / molar_mass2
    return (n_mol1 * R * t / volume) + (n_mol2 * R * t / volume)
