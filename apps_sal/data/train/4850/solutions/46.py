def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    Mass1, Mass2 = given_mass1 * 0.001/molar_mass1,  given_mass2 * 0.001/molar_mass2

    Temperature = temp + 273.15

    return (Mass1 + Mass2) *  0.082 * Temperature / volume * 1000

