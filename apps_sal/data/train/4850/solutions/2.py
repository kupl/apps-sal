def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    
# 1 - Calculate the amount of substance in moles
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
# 2 - Convert the temperature from Celcius to kelvin  
    Temp_Kelvin = temp + 273.15
# 3 - Enter the gas constant
    R = 0.082
# 4 - Calculate the ideal gas law       
    P1 = (n1 * R * Temp_Kelvin) / volume
    P2 = (n2 * R * Temp_Kelvin) / volume
# 5 - Apply Dalton's law
    P = P1 + P2
    return P
