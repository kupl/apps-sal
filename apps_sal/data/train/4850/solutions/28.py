def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    moles1 = given_mass1 / molar_mass1
    moles2 = given_mass2 / molar_mass2
    kelvin = temp + 273.15
    gas_constant = 0.082

    return (moles1 + moles2) * gas_constant * kelvin / volume
