def solution(m1, m2, M1, M2, V, t):
    n = (M1 / m1) + (M2 / m2)
    R = 0.082
    T = t + 273.15
    P = (n * R * T) / V
    return P


# Pressure (P),mercury/torr (mm Hg, torr)
# Volume (V), given in liters
# Number of moles of gas (n)
# R is the ideal gas constant
# Temperature of the gas (T) measured in degrees Kelvin (K)
