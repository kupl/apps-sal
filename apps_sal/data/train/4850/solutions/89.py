def solution(M1, M2, gm1, gm2, v, t) :
    Mass1 = gm1 * 0.001/M1
    Mass2 = gm2 * 0.001/M2
    temp = t + 273.15
    return ((((Mass1 + Mass2) * 0.082) * temp)/v) * 1000
    
    
    
#     For people wanting to do this kata, here is the formula:
# Mass1 = mole1 * 0.001/Mass1;

# Mass2 = mole2 * 0.001/Mass2;

# Temperature >> Convert to Kelvin (add 273.15)

# Answer => Combine Mass1 & Mass2, multiply by 0.082, multiply by Temperature, divide by the Volume, multiply by 1000

