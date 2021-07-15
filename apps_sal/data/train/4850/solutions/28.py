def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    # Find moles of given gasses
    moles1 = given_mass1 / molar_mass1
    moles2 = given_mass2 / molar_mass2
    # Convert Celcius to Kelvin
    kelvin = temp + 273.15
    gas_constant = 0.082
    
    # Given ideal gas law: PV = nRT
    # P = nRT/V                            (by algebra)
    # P = ((moles1 + moles2)RT)/V          (by substitution)
    return (moles1 + moles2) * gas_constant * kelvin / volume

