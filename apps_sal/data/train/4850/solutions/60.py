def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    # your code goes here
    mass1 = given_mass1 * 0.001/molar_mass1;
    mass2 = given_mass2 * 0.001/molar_mass2;
    temp = temp + 273.15
    return (mass1+mass2)*0.082*temp/volume*1000
