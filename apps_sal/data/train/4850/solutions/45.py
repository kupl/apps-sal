def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    #   Calculate the amount of substance in moles
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
#   Convert the temperature from Celcius to kelvin
    Temp_Kelvin = temp + 273.15
#   Enter the gas constant
    R_gasConst = 0.082
#   Calculate the ideal gas law
    P1 = (n1 * R_gasConst * Temp_Kelvin) / volume
    P2 = (n2 * R_gasConst * Temp_Kelvin) / volume
#   Dalton's law
    Pressure = P1 + P2

    return Pressure
