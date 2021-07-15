def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :  
    n1 = given_mass1 / molar_mass1  # хим. колличество вещества (моль)
    n2 = given_mass2 / molar_mass2  # хим. колличество вещества (моль)
    R = 0.082  # Универсальная газовая постоянная (литр * атм)/(Кельвин * моль)
    T = temp + 273.15  # Температура в Кельвинах
    V = volume  # Объём
    P = ((n1 + n2) * R * T) / V 
    return P

