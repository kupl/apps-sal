def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    n1=given_mass1/molar_mass1
    n2=given_mass2/molar_mass2
    T=273.15+temp
    R=0.082   #gas constant value
    return ((n1+n2)*R*T)/volume
    # your code goes here

