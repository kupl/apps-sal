def solution(m1, m2, g1, g2, v, t) :
#Mass1 = mole1 * 0.001/Mass1;
#Mass2 = mole2 * 0.001/Mass2;
#Temperature >> Convert to Kelvin (add 273.15)
#Combine Mass1 & Mass2, multiply by 0.082, multiply by Temperature, divide by the Volume, multiply by 1000
    return (g1 * 0.001 / m1 + g2 * 0.001 / m2) * 0.082 * (t + 273.15) / v * 1000
