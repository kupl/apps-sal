def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    # loi des gaz parfaits : PV=nRT
    # P = nRT/(V) on cherche n, le nombre de moles ... = m/M
    # pour un mélange, P = sum(Pi)
    # donc
    return ((given_mass1/molar_mass1)+(given_mass2/molar_mass2))*0.082*(temp+273.15)/volume
