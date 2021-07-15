def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    #P=nRT/V
    #no of molecules=total mass/molar mass
    n=(given_mass1/molar_mass1)+(given_mass2/molar_mass2)
    R=0.082
    Pressure=n*R*(temp+273.15)/volume
    return Pressure
