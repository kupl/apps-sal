def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    R = 0.082 #dm3.atm.K-1.mol-1
    T = 273.15 #Kelvin
    p1 = (given_mass1/molar_mass1)*R*(temp+T)/volume
    p2 = (given_mass2/molar_mass2)*R*(temp+T)/volume
    return (p1+p2)
