def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    print("define parametros")
    dm1 = molar_mass1
    dm2 = molar_mass2
    dg1 = given_mass1
    dg2 = given_mass2
    dvo = volume
    dte = temp
    return (0.082 / dvo) * (dg2 / dm2 + dg1 / dm1) * (dte + 273.15)
