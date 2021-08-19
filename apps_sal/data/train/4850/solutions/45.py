def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
    Temp_Kelvin = temp + 273.15
    R_gasConst = 0.082
    P1 = n1 * R_gasConst * Temp_Kelvin / volume
    P2 = n2 * R_gasConst * Temp_Kelvin / volume
    Pressure = P1 + P2
    return Pressure
